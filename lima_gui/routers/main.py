# main_chat_router.py
from fastapi import APIRouter, Request, UploadFile, File, HTTPException, Depends, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from lima_gui.models import Chat, Message, get_chat_db
import json

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
        chat = Chat(name="Imported Chat")
        for message in chat_data["messages"]:
            chat.messages.append(Message(role=message["role"], content=message["content"]))
        db.add(chat)
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
    chat_list = [{"id": chat.id, "name": chat.name, "message_count": len(chat.messages)} for chat in chats]
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
    new_chat = Chat(name="New Chat")
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return {"id": new_chat.id, "name": new_chat.name}


@main_router.post("/chats/{chat_id}/copy")
def copy_chat(chat_id: int, db: Session = Depends(get_chat_db)):
    original_chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not original_chat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found")
        
    copied_chat = Chat(name=f"{original_chat.name} - Copy")
    for message in original_chat.messages:
        copied_chat.messages.append(Message(role=message.role, content=message.content))
    
    db.add(copied_chat)
    db.commit()
    db.refresh(copied_chat)
    return {"id": copied_chat.id, "name": copied_chat.name}