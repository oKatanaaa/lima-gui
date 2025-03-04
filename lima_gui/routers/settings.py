# In routers/settings.py
from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from typing import Optional


settings_router = APIRouter(prefix="/settings")


class OpenAIConfig(BaseModel):
    model: str
    temperature: float
    api_key: Optional[str] = None
    # other fields...

def get_config_manager(request: Request):
    return request.app.state.config_manager

@settings_router.get("/openai")
def get_openai_settings(config_manager = Depends(get_config_manager)):
    return config_manager.get_openai_config()

@settings_router.post("/openai")
def update_openai_settings(
    config: OpenAIConfig,
    config_manager = Depends(get_config_manager)
):
    current_config = config_manager.get_openai_config()
    # Update only the fields that were provided
    updated_config = {**current_config, **config.dict(exclude_unset=True)}
    config_manager.save_openai_config(updated_config)
    return {"status": "success"}