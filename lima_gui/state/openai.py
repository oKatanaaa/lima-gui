import openai
import time

OPEN_AI_DEFAULT_API_BASE = openai.api_base


class OpenAIService: 
    instance = None
    
    DEFAULT_MODEL = 'gpt-3.5-turbo'
    DEFAULT_TEMPERATURE = 0.7
       
    @staticmethod
    def get_instance():
        if OpenAIService.instance is None:
            OpenAIService.instance = OpenAIService()
        return OpenAIService.instance
    
    def __init__(self):
        assert OpenAIService.instance is None, 'OpenAIService instance already exists. Please use get_instance method.'
        self.model = OpenAIService.DEFAULT_MODEL
        self.temperature = OpenAIService.DEFAULT_TEMPERATURE
        self.enabled = False

    def set_model(self, model):
        self.model = model
    
    def set_temperature(self, temperature):
        self.temperature = float(temperature)
        
    def set_api_base(self, api_base):
        if len(api_base) == 0:
            api_base = OPEN_AI_DEFAULT_API_BASE
        
        openai.api_base = api_base
    
    def set_api_key(self, api_key):
        openai.api_key = api_key

    def generate_response(self, conversation):
        print(conversation)
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=conversation,
            temperature=self.temperature,
            stream=True
        )
        iterator = iter(response)
        while True:
            start_time = time.time()
            try:
                chunk = next(iterator)
                delta_time = time.time() - start_time
                delta_text = chunk['choices'][0]['delta']
                if 'content' not in delta_text:
                    continue
                yield delta_time, delta_text['content']
            except StopIteration:
                break
