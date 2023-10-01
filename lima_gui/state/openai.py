import openai
import time

OPEN_AI_DEFAULT_API_BASE = openai.api_base


class OpenAIService: 
    instance = None
    API_TYPE_CHAT = 'chat'
    API_TYPE_COMPLETION = 'completion'
    
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
        self.api_type = OpenAIService.API_TYPE_CHAT
        self.max_completion_tokens = 200

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
        
    def get_api_types(self):
        return [OpenAIService.API_TYPE_CHAT, OpenAIService.API_TYPE_COMPLETION]
    
    def get_api_type(self):
        return self.api_type

    def set_api_type(self, api_type):
        assert api_type in self.get_api_types(), 'Invalid API type.'
        self.api_type = api_type

    def generate_response(self, conversation, context=None):
        if self.api_type == OpenAIService.API_TYPE_CHAT:
            return self._chat_response(conversation)
        elif self.api_type == OpenAIService.API_TYPE_COMPLETION:
            return self._completion_response(conversation, context)
        else:
            raise Exception('Invalid API type.')
            
    def _chat_response(self, conversation):
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
    
    def _completion_response(self, conversation, context):
        # Convert conversation into a single prompt
        prompt = ""
        for msg in conversation:
            role = msg['role']
            content = msg['content']
            prompt += f'<{role}>\n{content}<end>'
        
        assert role == 'user', 'User role is required as the last role.'
        before, after = context
        prompt += f'<assistant>\n{before}<end>'
        
        response = openai.Completion.create(
            model=self.model,
            prompt=prompt,
            suffix=after,
            temperature=self.temperature,
            max_tokens=self.max_completion_tokens,
            stream=True
        )
        iterator = iter(response)
        while True:
            start_time = time.time()
            try:
                chunk = next(iterator)
                delta_time = time.time() - start_time
                delta_text = chunk['choices'][0]
                if 'text' not in delta_text:
                    continue
                yield delta_time, delta_text['text']
            except StopIteration:
                break
