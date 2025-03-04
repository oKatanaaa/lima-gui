from sqlalchemy.orm import Session
from lima_gui.models import Chat, Message
from pydantic import BaseModel
from typing import Any, List, Optional


class ToolSchema(BaseModel):
    name: str
    description: str
    parameters: str

class ToolCallSchema(BaseModel):
    id: str
    tool_name: str

class MessageSchema(BaseModel):
    id: int
    role: str
    content: str
    tool_calls: List[ToolCallSchema]

    @staticmethod
    def from_orm(msg: Message):
        tools = []
        for tc in msg.tool_calls:
            tools.append(ToolCallSchema(
                id=tc.id,
                tool_name=tc.name
            ))

        return MessageSchema(
            id=msg.id,
            role=msg.role,
            content=msg.content,
            tool_call=tools
        )

class ChatDetailsSchema(BaseModel):
    id: int
    name: str
    n_msgs: int
    n_tokens: int
    messages: List[MessageSchema]


def calculate_tokens(content: str) -> int:
    # Placeholder function to calculate tokens
    return len(content.split())

def get_chat(chat_id: int, db: Session) -> Optional[ChatDetailsSchema]:
    chat = db.query(Chat).get(chat_id)
    if not chat:
        return None

    ordered_messages = sorted(chat.messages, key=lambda msg: msg.position)
    messages = [MessageSchema.from_orm(msg) for msg in ordered_messages]
    n_tokens = sum(calculate_tokens(message.content) for message in chat.messages)
    n_msgs = len(chat.messages)

    return ChatDetailsSchema(
        id=chat.id,
        name=chat.name,
        n_msgs=n_msgs,
        n_tokens=n_tokens,
        messages=messages
    )

def add_message(chat_id: int, db: Session) -> MessageSchema:
    chat = db.query(Chat).get(chat_id)
    role = "system"
    last_position = max((msg.position for msg in chat.messages), default=0)

    last_message = chat.messages[-1] if chat.messages else None

    if last_message is not None:
        role = "user" if last_message.role == "assistant" else "assistant"

    msg = Message(
        role=role, 
        content="", 
        chat=chat, 
        position=last_position + 1,
        tool_calls=[]
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)

    return MessageSchema.from_orm(msg)