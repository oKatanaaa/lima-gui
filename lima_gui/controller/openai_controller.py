from lima_gui.state import OpenAIService
from lima_gui.view.openai_window import OpenaiWindow


class OpenAIController:
    def __init__(self, window: OpenaiWindow):
        self.window =  window
        self.service = OpenAIService.get_instance()
        
        self.window.set_api_enabled_callback(self.on_api_enabled)
        self.window.set_settings_changed_callback(self.on_settings_changed)
        self.window.set_api_types(
            self.service.get_api_types(), self.service.get_api_type())
        
    def on_api_enabled(self, enabled):
        print('enabled openai api', enabled > 0)
        self.service.enabled = enabled > 0
    
    def on_settings_changed(self, api_base, api_key, model, temp, api_type):
        print(
            f'api_base: {api_base}, api_key: {api_key}, model: {model}, temp: {temp}', 'api_type: ', api_type
        )
        assert api_type in ('chat', 'completion')
        self.service.set_api_base(api_base)
        self.service.set_api_key(api_key)
        self.service.set_model(model)
        self.service.set_temperature(temp)
        self.service.set_api_type(api_type)
