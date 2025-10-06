from fastapi import APIRouter, Request, UploadFile, File, HTTPException, Depends, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from lima_gui.models import Chat, Message, Tool, ToolCall, Tag, get_chat_db
from lima_gui.models.chat import RoleEnum
import json
from ..services.chat import get_chat as _get_chat
from ..services.chat import add_message as _add_message
from ..services.chat import ChatDetailsSchema, MessageSchema, ToolSchema
from typing import List

"""
Functionality:

--- chat level ---
0. Get chat - get_chat
1. Edit chat name and tags - update_chat
2. Add a tool - add_tool
3. Edit a tool - edit_tool
4. Delete a tool.

--- message level ---
1. Add a message.
2. Update a message.
- Edit content.
- Edit role.
3. Delete a message.
4. For a given message add a tool call.
5. For a given message edit a tool call.
"""

chat_router = APIRouter(prefix="/chat")


@chat_router.get("/{id}", response_model=ChatDetailsSchema)
async def get_chat(id: int, db: Session = Depends(get_chat_db)):
    chat = _get_chat(id, db)

    if not chat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found")
    
    return chat


@chat_router.put("/{id}", response_model=ChatDetailsSchema)
async def update_chat(id: int, request: Request, db: Session = Depends(get_chat_db)):
    data = await request.json()

    if not isinstance(data, dict):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Payload must be a JSON object",
        )
    chat = db.query(Chat).get(id)

    if not chat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found")

    name = data.get("name")
    if name is not None:
        chat.name = name

    language = data.get("language")
    if language is not None:
        chat.language = language

    if "tags" in data:
        raw_tags = data.get("tags") or []

        if not isinstance(raw_tags, list):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Tags must be provided as a list")

        existing_tags = {}
        if raw_tags:
            db_tags = db.query(Tag).filter(Tag.name.in_(raw_tags)).all()
            existing_tags = {tag.name: tag for tag in db_tags}

        new_tag_objects = []
        seen = set()
        for tag_name in raw_tags:
            if not isinstance(tag_name, str):
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Each tag must be a string")

            tag_name = tag_name.strip()
            if not tag_name or tag_name in seen:
                continue
            seen.add(tag_name)

            tag_obj = existing_tags.get(tag_name)
            if not tag_obj:
                tag_obj = Tag(name=tag_name)
                db.add(tag_obj)
                existing_tags[tag_name] = tag_obj

            new_tag_objects.append(tag_obj)

        chat.tags = new_tag_objects

    db.commit()

    updated_chat = _get_chat(id, db)
    if updated_chat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found")

    return updated_chat


@chat_router.post("/{id}/tools", response_model=ToolSchema)
async def add_tool(id: int, request: Request, db: Session = Depends(get_chat_db)):
    data = await request.json()
    chat = db.query(Chat).get(id)
    name = data["name"]
    description = data["description"]
    parameters = data["parameters"]

    tool = Tool(name=name, description=description, parameters=parameters, chat=chat)
    chat.tools.append(tool)
    db.commit()
    db.refresh(tool)

    tool_schema = ToolSchema(
        name=tool.name,
        description=tool.description,
        parameters=tool.parameters
    )
    return tool_schema


@chat_router.put("/{id}/tools/{tool_name}")
async def edit_tool(id: int, tool_name: str, request: Request, db: Session = Depends(get_chat_db)):
    data = await request.json()
    tool = db.query(Tool).filter(Tool.chat_id == id, Tool.name == tool_name).first()
    tool.name = data["name"]
    tool.description = data["description"]
    tool.parameters = data["parameters"]
    db.commit()
    return {"status": "success", "message": "Tool updated"}


@chat_router.delete("/{id}/tools/{tool_name}")
async def delete_tool(id: int, tool_name: str, db: Session = Depends(get_chat_db)):
    tool = db.query(Tool).filter(Tool.chat_id == id, Tool.name == tool_name).first()

    if not tool:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tool not found")

    db.delete(tool)
    db.commit()

    return {"status": "success", "detail": "Tool deleted"}


# --- MESSAGE LEVEL ---


@chat_router.post("/{id}/message", response_model=MessageSchema)
async def add_message(id: int, db: Session = Depends(get_chat_db)):
    msg = _add_message(id, db)
    return msg


@chat_router.put("/{id}/message/{message_id}", response_model=MessageSchema)
async def update_message(id: int, message_id: int, request: Request, db: Session = Depends(get_chat_db)):
    data = await request.json()

    if not isinstance(data, dict):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Payload must be a JSON object",
        )

    message = db.query(Message).filter(Message.id == message_id, Message.chat_id == id).first()

    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

    updated = False

    if "content" in data:
        content_value = data["content"]

        if content_value is None:
            content_value = ""
        elif not isinstance(content_value, str):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Content must be a string",
            )

        message.content = content_value
        updated = True

    if "role" in data:
        role_value = data["role"]
        if role_value is None:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Role cannot be null")

        if isinstance(role_value, str):
            role_value = role_value.strip()

        if not isinstance(role_value, str):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Role must be a string",
            )

        if not role_value:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Role cannot be empty",
            )

        try:
            role_enum = RoleEnum(role_value.lower())
        except ValueError:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid role value")

        message.role = role_enum
        updated = True

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No supported fields provided for update",
        )

    db.commit()
    db.refresh(message)

    return MessageSchema.from_orm(message)


@chat_router.delete("/{chat_id}/message/{message_id}")
async def delete_message(chat_id: int, message_id: int, db: Session = Depends(get_chat_db)):
    message = db.query(Message).filter(
        Message.id == message_id,
        Message.chat_id == chat_id,
    ).first()

    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

    db.delete(message)
    db.commit()

    # Reorder remaining messages
    remaining_messages = (
        db.query(Message)
        .filter(Message.chat_id == chat_id)
        .order_by(Message.position)
        .all()
    )

    for index, msg in enumerate(remaining_messages):
        msg.position = index + 1  # Reassign position starting from 1

    db.commit()

    return {"status": "success", "detail": "Message deleted and reordered"}


@chat_router.post("/{chat_id}/message/{message_id}/tool_call")
async def add_tool_call(chat_id: int, message_id: int, request: Request, db: Session = Depends(get_chat_db)):
    data = await request.json()
    message = db.query(Message).filter(Message.id == message_id, Message.chat_id == chat_id).first()
    name = data["name"]
    arguments = data["arguments"]
    tool_call = ToolCall(name=name, arguments=arguments, message=message)
    message.tool_calls.append(tool_call)
    db.commit()
    db.refresh(tool_call)

    return {"status": "success", "message": "Tool call added"}


@chat_router.put("/{chat_id}/message/{message_id}/tool_call/{tool_call_id}")
async def edit_tool_call(chat_id: int, message_id: int, tool_call_id: int, request: Request, db: Session = Depends(get_chat_db)):
    data = await request.json()
    tool_call = db.query(ToolCall).filter(ToolCall.id == tool_call_id, ToolCall.message_id == message_id).first()
    tool_call.name = data["name"]
    tool_call.arguments = data["arguments"]
    db.commit()
    return {"status": "success", "message": "Tool call updated"}