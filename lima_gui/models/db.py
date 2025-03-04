import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
import appdirs
from pathlib import Path
from lima_gui.constants import APP_NAME

def get_app_data_dir():
    """Get the platform-specific application data directory."""
    app_dir = Path(appdirs.user_data_dir(APP_NAME))
    app_dir.mkdir(parents=True, exist_ok=True)
    return app_dir


def get_chat_db_url():
    """Get database URL for chat database with proper user directory."""
    # Check if environment variable is set
    if os.getenv("CHAT_DB_URL"):
        return os.getenv("CHAT_DB_URL")
    
    # Use platform-specific user data directory
    db_path = get_app_data_dir() / "chat.db"
    return f"sqlite:///{db_path}"


def init_databases():
    """Initialize all databases if they don't exist."""
    # Get engines
    chat_engine = get_chat_engine()
    
    # Create all tables if they don't exist
    from .chat import ChatBase
    
    ChatBase.metadata.create_all(chat_engine)
    
    # Log initialization
    from loguru import logger
    logger.info(f"Initialized databases at {get_app_data_dir()}")


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

