from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from lima_gui.routers import main_router, chat_router, settings_router
from lima_gui.models.db import init_databases
from lima_gui.config import ConfigManager
from fastapi.middleware.cors import CORSMiddleware


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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(main_router)
app.include_router(chat_router)
app.include_router(settings_router)

# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse
# import os

# # Serve React build directory
# frontend_build_dir = os.path.join(os.path.dirname(__file__), "..", "frontend", "build")
# if os.path.exists(frontend_build_dir):
#     app.mount("/static", StaticFiles(directory=f"{frontend_build_dir}/static"), name="static")

#     @app.get("/{full_path:path}")
#     async def serve_react_app(full_path: str):
#         # Serve API requests normally
#         if full_path.startswith("api/"):
#             raise HTTPException(status_code=404, detail="Not found")
        
#         # For all other routes, serve the React app
#         return FileResponse(f"{frontend_build_dir}/index.html")
