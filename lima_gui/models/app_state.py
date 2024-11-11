from sqlalchemy import Boolean, Float, Enum, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, Integer, String, Enum, Text
)
from sqlalchemy.orm import validates
import enum
import json
from sqlalchemy.orm import sessionmaker


AppStateBase = declarative_base()


class ApiTypeEnum(enum.Enum):
    chat = "chat"
    completion = "completion"


class OpenAICredentials(AppStateBase):
    __tablename__ = 'openai_credentials'

    id = Column(Integer, primary_key=True)
    enabled = Column(Boolean, default=False)
    model = Column(String, default="gpt-4o-mini")
    temperature = Column(Float, CheckConstraint("temperature >= 0 AND temperature <= 2"))
    api_type = Column(Enum(ApiTypeEnum), nullable=False, default=ApiTypeEnum.chat)
    max_completion_tokens = Column(Integer, default=100)
    api_base = Column(String, nullable=True)
    api_key = Column(String, nullable=True)
    extra_body = Column(Text, nullable=True)

    @validates("extra_body")
    def validate_extra_body(self, key, value):
        if value:
            try:
                json.loads(value)  # Ensure `extra_body` is valid JSON
            except json.JSONDecodeError:
                raise ValueError("extra_body must be a valid JSON string.")
        return value


from .db import get_state_engine


def init_state():
    engine = get_state_engine()
    AppStateBase.metadata.create_all(engine)
