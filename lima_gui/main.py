from contextlib import asynccontextmanager
from fastapi import FastAPI
from lima_gui.routers import main_router, chat_router, settings_router
from lima_gui.models.db import init_databases
from lima_gui.config import ConfigManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize config manager (makes it available for the whole app)
    app.state.config_manager = ConfigManager()

    # Initialize databases
    init_databases()
    
    # Log application startup
    from loguru import logger
    logger.info("LIMA-GUI application started")
    
    yield
    
    # Log application shutdown
    logger.info("LIMA-GUI application stopped")


app = FastAPI(lifespan=lifespan)
app.include_router(main_router)
app.include_router(chat_router)
app.include_router(settings_router)