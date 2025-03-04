import os
import json
from pathlib import Path
import appdirs
from typing import Dict, Any, Optional
from lima_gui.constants import APP_NAME

class ConfigManager:
    """Manages application configuration using JSON files in the user config directory."""
    
    def __init__(self):
        # Get platform-specific config directory
        self.config_dir = Path(appdirs.user_config_dir(APP_NAME))
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        # Define file paths
        self.openai_config_path = self.config_dir / "openai_config.json"
        self.app_config_path = self.config_dir / "app_config.json"
        
        # Initialize default configs if they don't exist
        self._ensure_default_configs()
    
    def _ensure_default_configs(self):
        """Create default configuration files if they don't exist."""
        # Default OpenAI configuration
        if not self.openai_config_path.exists():
            default_openai_config = {
                "enabled": False,
                "model": "gpt-4o-mini",
                "temperature": 0.7,
                "api_type": "chat",
                "max_completion_tokens": 100,
                "api_base": None,
                "api_key": None,
                "extra_body": None
            }
            self.save_openai_config(default_openai_config)
        
        # Default app configuration
        if not self.app_config_path.exists():
            default_app_config = {
                "tokenizer": "mistralai/Mistral-7B-v0.1",
                "theme": "light",
                "languages": ["en", "ru"],
                "default_language": "en"
            }
            self.save_app_config(default_app_config)
    
    def get_openai_config(self) -> Dict[str, Any]:
        """Get the OpenAI API configuration."""
        if not self.openai_config_path.exists():
            return self._ensure_default_configs()
        
        with open(self.openai_config_path, 'r') as f:
            return json.load(f)
    
    def save_openai_config(self, config: Dict[str, Any]) -> None:
        """Save the OpenAI API configuration."""
        with open(self.openai_config_path, 'w') as f:
            json.dump(config, f, indent=2)
    
    def get_app_config(self) -> Dict[str, Any]:
        """Get the application configuration."""
        if not self.app_config_path.exists():
            return self._ensure_default_configs()
        
        with open(self.app_config_path, 'r') as f:
            return json.load(f)
    
    def save_app_config(self, config: Dict[str, Any]) -> None:
        """Save the application configuration."""
        with open(self.app_config_path, 'w') as f:
            json.dump(config, f, indent=2)
    
    def get_config_dir(self) -> Path:
        """Get the configuration directory path."""
        return self.config_dir