# main_chat_router.py
from fastapi import APIRouter, Request, UploadFile, File, HTTPException, Depends, status, Query
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from lima_gui.models import Chat, Message, Tool, Tag, ToolCall, get_chat_db
from lima_gui.services.chat import calculate_tokens, ToolSchema
from lima_gui.services.file_service import FileService
import json
import tempfile
import os
import copy

# Create a new router that handles both main page and chat functionalities
main_router = APIRouter()

# Setup Jinja2 template engine
templates = Jinja2Templates(directory="lima_gui/view")

# --- Main Page Rendering ---
@main_router.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@main_router.post("/chats/upload")
async def upload_chat(file: UploadFile = File(...), db: Session = Depends(get_chat_db)):
    if file.content_type != "application/jsonl":
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, 
            detail="Only JSONL files are supported"
        )

    content = await file.read()
    chats_data = [json.loads(line) for line in content.decode().splitlines()]

    for chat_data in chats_data:
        chat_name = chat_data.get("name") or "Imported Chat"
        language = chat_data.get("language") or "en"
        chat = Chat(name=chat_name, language=language)
        db.add(chat)

        raw_tags = chat_data.get("tags") or []
        if raw_tags:
            db_tags = db.query(Tag).filter(Tag.name.in_(raw_tags)).all()
            tag_lookup = {tag.name: tag for tag in db_tags}
            seen = set()
            for tag_name in raw_tags:
                if not isinstance(tag_name, str):
                    continue
                normalized = tag_name.strip()
                if not normalized or normalized in seen:
                    continue
                seen.add(normalized)
                tag_obj = tag_lookup.get(normalized)
                if not tag_obj:
                    tag_obj = Tag(name=normalized)
                    db.add(tag_obj)
                    tag_lookup[normalized] = tag_obj
                chat.tags.append(tag_lookup[normalized])

        for tool_data in chat_data.get("tools", []):
            if not isinstance(tool_data, dict):
                continue
            db.add(
                Tool(
                    name=tool_data.get("name"),
                    description=tool_data.get("description"),
                    parameters=copy.deepcopy(tool_data.get("parameters")),
                    chat=chat,
                )
            )

        for index, message_data in enumerate(chat_data.get("messages", []), start=1):
            if not isinstance(message_data, dict):
                continue
            role = message_data.get("role", "system")
            content = message_data.get("content", "")
            position = message_data.get("position") or index
            new_message = Message(
                role=role,
                content=content,
                position=position,
                chat=chat,
            )
            db.add(new_message)

            for tool_call in message_data.get("tool_calls", []):
                if not isinstance(tool_call, dict):
                    continue
                db.add(
                    ToolCall(
                        tool_call_id=tool_call.get("tool_call_id"),
                        name=tool_call.get("name"),
                        arguments=tool_call.get("arguments"),
                        message=new_message,
                    )
                )
    db.commit()
    return {
        "status": "success", 
        "message": "File uploaded and processed successfully."
    }


@main_router.get("/chats/save")
def save_chats(db: Session = Depends(get_chat_db)):
    chats = db.query(Chat).all()
    response_data = []
    for chat in chats:
        chat_data = {
            "messages": [{"role": message.role, "content": message.content} for message in chat.messages]
        }
        response_data.append(chat_data)
    return "\n".join(json.dumps(line) for line in response_data)


@main_router.get("/chats")
def fetch_chats(db: Session = Depends(get_chat_db)):
    chats = db.query(Chat).all()
    chat_list = []
    for chat in chats:
        tokens = sum(calculate_tokens(message.content) for message in chat.messages)
        chat_list.append({
            "id": chat.id,
            "name": chat.name,
            "message_count": len(chat.messages),
            "language": chat.language,
            "tags": [tag.name for tag in chat.tags],
            "tools": [ToolSchema.from_orm(tool).model_dump() for tool in chat.tools],
            "tokens": tokens,
        })
    return chat_list


@main_router.delete("/chats/{chat_id}")
def delete_chat(chat_id: int, db: Session = Depends(get_chat_db)):
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found")
    db.delete(chat)
    db.commit()
    return {"status": "success", "message": f"Chat {chat_id} deleted"}


@main_router.post("/chats")
def add_chat(db: Session = Depends(get_chat_db)):
    new_chat = Chat(name="New Chat", language="en")
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return {"id": new_chat.id, "name": new_chat.name}


@main_router.post("/chats/{chat_id}/copy")
def copy_chat(chat_id: int, db: Session = Depends(get_chat_db)):
    original_chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not original_chat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found")
        
    copied_chat = Chat(
        name=f"{original_chat.name} - Copy",
        language=original_chat.language or "en",
    )

    db.add(copied_chat)

    copied_chat.tags = list(original_chat.tags)

    for tool in original_chat.tools:
        db.add(
            Tool(
                name=tool.name,
                description=tool.description,
                parameters=copy.deepcopy(tool.parameters),
                chat=copied_chat,
            )
        )

    ordered_messages = sorted(original_chat.messages, key=lambda msg: msg.position)
    for message in ordered_messages:
        role_value = message.role.value if hasattr(message.role, "value") else message.role
        new_message = Message(
            role=role_value,
            content=message.content,
            position=message.position,
            chat=copied_chat,
        )
        db.add(new_message)

        for tool_call in message.tool_calls:
            db.add(
                ToolCall(
                    tool_call_id=tool_call.tool_call_id,
                    name=tool_call.name,
                    arguments=tool_call.arguments,
                    message=new_message,
                )
            )

    db.commit()
    db.refresh(copied_chat)
    return {"id": copied_chat.id, "name": copied_chat.name}


@main_router.post("/import")
async def import_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_chat_db)
):
    """Import chats from a JSONL file."""
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jsonl") as temp_file:
        temp_file.write(await file.read())
        temp_path = temp_file.name
    
    try:
        # Import the file
        file_service = FileService(db)
        chats_added = file_service.import_jsonl(temp_path)
        
        return {
            "status": "success",
            "chats_added": chats_added,
            "message": f"Successfully imported {chats_added} chats"
        }
    finally:
        # Clean up temp file
        os.unlink(temp_path)


@main_router.get("/export")
async def export_file(
    filename: str = Query("lima-chats.jsonl", description="Export filename"),
    db: Session = Depends(get_chat_db)
):
    """Export all chats to a JSONL file."""
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jsonl") as temp_file:
        temp_path = temp_file.name
    
    try:
        # Export to the file
        file_service = FileService(db)
        chats_exported = file_service.export_jsonl(temp_path)
        
        # Return the file
        return FileResponse(
            path=temp_path,
            filename=filename,
            media_type="application/jsonl",
            background=lambda: os.unlink(temp_path)  # Delete after sending
        )
    except Exception:
        # Clean up on error
        os.unlink(temp_path)
        raise