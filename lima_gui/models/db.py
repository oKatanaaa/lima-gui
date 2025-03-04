import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv

load_dotenv()

def get_chat_db_url():
    return os.getenv("CHAT_DB_URL", "sqlite:///./chat.db")

def get_state_db_url():
    return os.getenv("STATE_DB_URL", "sqlite:///./state.db")


_chat_engine = None
_chat_session = None


def get_chat_engine():
    global _chat_engine
    if _chat_engine is None:
        _chat_engine = create_engine(get_chat_db_url(), echo=True)
    return _chat_engine


def get_chat_session():
    global _chat_session
    if _chat_session is None:
        _chat_session = scoped_session(sessionmaker(bind=get_chat_engine()))
    return _chat_session


# Dependency to use a session in endpoints
def get_chat_db():
    db = get_chat_session()
    try:
        yield db
    finally:
        db.remove()

# --- For App State ---

_state_engine = None
_state_session = None

def get_state_engine():
    global _state_engine
    if _state_engine is None:
        _state_engine = create_engine(get_state_db_url(), echo=True)
    return _state_engine


def get_state_session():
    global _state_session
    if _state_session is None:
        _state_session = scoped_session(sessionmaker(bind=get_state_engine()))
    return _state_session


# Dependency to use a session in endpoints
def get_state_db():
    db = get_state_session()
    try:
        yield db
    finally:
        db.remove()