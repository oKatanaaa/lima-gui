from fastapi import APIRouter, Request, UploadFile, File, HTTPException, Depends, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from lima_gui.models import Chat, Message, get_chat_db
import json
from ..services.chat import get_chat as _get_chat
from ..services.chat import add_message as _add_message
from ..services.chat import ChatDetailsSchema, MessageSchema


chat_router = APIRouter(prefix="/chat")


@chat_router.get("/{id}")
async def get_chat(id: int, db: Session = Depends(get_chat_db)) -> ChatDetailsSchema:
    chat = _get_chat(id, db)

    if not chat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found")
    
    return chat


@chat_router.post("/{id}/message")
async def add_message(id: int, db: Session = Depends(get_chat_db)):
    msg = _add_message(id, db)
    return msg


@chat_router.put("/{id}/message/{message_id}")
async def update_message(id: int, message_id: int, request: Request, db: Session = Depends(get_chat_db)):
    data = await request.json()
    chat = db.query(Chat).get(id)
    message = db.query(Message).get(message_id)
    message.content = data["content"]
    db.commit()
    return {"status": "success", "message": "Message updated"}


@chat_router.delete("/{chat_id}/message/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_message(chat_id: int, message_id: int, db: Session = Depends(get_chat_db)):
    # Fetch the specified message
    message = db.query(Message).filter(Message.id == message_id, Message.chat_id == chat_id).first()
    
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

    # Delete the message
    db.delete(message)
    db.commit()

    # Reorder remaining messages
    remaining_messages = db.query(Message).filter(Message.chat_id == chat_id).order_by(Message.position).all()
    
    for index, msg in enumerate(remaining_messages):
        msg.position = index + 1  # Reassign position starting from 1

    db.commit()

    return {"status": "success", "detail": "Message deleted and reordered"}

