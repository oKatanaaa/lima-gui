from sqlalchemy import (
    create_engine, Column, Integer, String, 
    ForeignKey, Enum, Table, Text, UniqueConstraint, PrimaryKeyConstraint
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, validates
from sqlalchemy.types import JSON
import enum
import jsonschema
from jsonschema import validate


ChatBase = declarative_base()

class RoleEnum(enum.Enum):
    system = "system"
    user = "user"
    assistant = "assistant"
    tool = "tool"

# Association table for Chat <-> Tag many-to-many relationship
chat_tag_association = Table(
    "chat_tag", ChatBase.metadata,
    Column("chat_id", Integer, ForeignKey("chats.id")),
    Column("tag_name", String, ForeignKey("tags.name"))  # Reference `Tag.name`
)

# Tag model with `name` as the primary key
class Tag(ChatBase):
    __tablename__ = 'tags'

    name = Column(String, primary_key=True)  # Tag is uniquely identified by `name`


class Chat(ChatBase):
    __tablename__ = 'chats'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    messages = relationship("Message", back_populates="chat", cascade="all, delete-orphan")
    tools = relationship("Tool", back_populates="chat", cascade="all, delete-orphan")
    tags = relationship("Tag", secondary=chat_tag_association, backref="chats")


class Message(ChatBase):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey('chats.id'))
    role = Column(Enum(RoleEnum), nullable=False)
    content = Column(String)
    position = Column(Integer, nullable=False)
    chat = relationship("Chat", back_populates="messages")
    tool_calls = relationship("ToolCall", back_populates="message", cascade="all, delete-orphan")


class ToolCall(ChatBase):
    __tablename__ = 'tool_calls'

    id = Column(Integer, primary_key=True)
    tool_call_id = Column(Integer, nullable=True)  # External ID for ToolCall, not primary key
    name = Column(String, nullable=False)
    arguments = Column(Text, nullable=True)
    message_id = Column(Integer, ForeignKey('messages.id'))
    message = relationship("Message", back_populates="tool_calls")


class Tool(ChatBase):
    __tablename__ = 'tools'

    chat_id = Column(Integer, ForeignKey('chats.id'))
    name = Column(String, nullable=False)
    description = Column(String)
    parameters = Column(JSON, nullable=True)
    chat = relationship("Chat", back_populates="tools")

    # Ensure tool names are unique within each chat
    __table_args__ = (
        PrimaryKeyConstraint('chat_id', 'name', name='pk_tool_chat_name'),
    )

    # Validate that parameters, if present, is a valid JSON schema
    @validates("parameters")
    def validate_parameters(self, key, value):
        if value:
            try:
                validate(instance={}, schema=value)  # Basic validation with an empty instance
            except jsonschema.exceptions.ValidationError as e:
                raise ValueError(f"Invalid JSON schema: {e.message}")
        return value


from .db import get_chat_engine


def init_chat():
    engine = get_chat_engine()
    ChatBase.metadata.create_all(engine)
