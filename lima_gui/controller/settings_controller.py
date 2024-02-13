import json

from lima_gui.logging import all_methods_logger
from lima_gui.view.settings_window import SettingsWindow
from lima_gui.state.settings import Settings


@all_methods_logger
class SettingsController:
    def __init__(self, settings_window: SettingsWindow):
        self.settings_window = settings_window
        self.settings = Settings.get_instance()

        self.settings_window.set_set_tokenizer_callback(self.on_set_tokenizer_clicked)
        self.settings_window.set_load_config_callback(self.on_load_config_clicked)
        
        self.set_window_data()
        
    def on_set_tokenizer_clicked(self, tokenizer_name):
        self.settings.set_tokenizer(tokenizer_name)
        
    def on_load_config_clicked(self, filename):
        with open(filename, 'r') as f:
            config = json.load(f)
        
        self.settings.set_tokenizer(config['tokenizer'])
        self.settings.tags = config['tags']
        # Not displayed at the moment
        self.settings.languages = config.get('languages', ['en', 'ru'])
        
        self.set_window_data()
    
    def set_window_data(self):
        self.settings_window.set_tags(self.settings.tags)
        self.settings_window.set_tokenizer_name(self.settings.tokenizer_name)
