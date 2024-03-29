from openai import OpenAI, base_url
import time
from typing import List, Optional
import json
from loguru import logger

from ..model.function import Tool
from lima_gui.logging import all_methods_logger

OPEN_AI_DEFAULT_API_BASE = base_url


@all_methods_logger
class OpenAIService: 
    instance: Optional['OpenAIService'] = None
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
        self.api_base = OPEN_AI_DEFAULT_API_BASE
        self.api_key = ''

    def set_model(self, model):
        self.model = model
    
    def set_temperature(self, temperature):
        self.temperature = float(temperature)
        
    def set_api_base(self, api_base):
        if len(api_base) == 0:
            api_base = OPEN_AI_DEFAULT_API_BASE
        
        self.api_base = api_base
    
    def set_api_key(self, api_key):
        self.api_key = api_key
        
    def get_api_types(self):
        return [OpenAIService.API_TYPE_CHAT, OpenAIService.API_TYPE_COMPLETION]
    
    def get_api_type(self):
        return self.api_type

    def set_api_type(self, api_type):
        assert api_type in self.get_api_types(), 'Invalid API type.'
        self.api_type = api_type
    
    @property
    def openai(self):
        return OpenAI(api_key=self.api_key, base_url=self.api_base)

    def generate_response(self, conversation, context=None, functions: Optional[List[Tool]] = None):
        if self.api_type == OpenAIService.API_TYPE_CHAT:
            return self._chat_response(conversation, functions)
        elif self.api_type == OpenAIService.API_TYPE_COMPLETION:
            return self._completion_response(conversation, context)
        else:
            logger.exception('Invalid API type.', api_type=self.api_type)
            raise Exception('Invalid API type.')
            
    def _chat_response(self, conversation, functions: Optional[List[Tool]] = None):
        for msg in conversation:
            if 'function_call' in msg and 'arguments' in msg['function_call']:
                msg['function_call']['arguments'] = json.dumps(msg['function_call']['arguments'])
        if functions is not None:
            functions = [f.to_openai_dict() for f in functions]
            logger.debug('when generating response received functions', functions)
            logger.debug('when generating response received conversation', conversation)
            response = self.openai.chat.completions.create(
                model=self.model,
                messages=conversation,
                tools=functions,
                temperature=self.temperature,
                stream=True
            )
        else:
            logger.debug('no functions is provided')
            response = self.openai.chat.completions.create(
                model=self.model,
                messages=conversation,
                temperature=self.temperature,
                stream=True
            )
            
        start_time = time.time()
        for chunk in response:
            logger.debug('chunk ' + repr(chunk))
            delta_time = time.time() - start_time
            delta = chunk.choices[0].delta
            if delta.content is not None:
                yield delta_time, delta.content
            if delta.tool_calls is not None:
                fn_call = delta.tool_calls[0].function
                delta_dict = {'name': fn_call.name, 'arguments': fn_call.arguments}
                yield delta_time, delta_dict
            start_time = time.time()
    
    def _completion_response(self, conversation, context):
        # Convert conversation into a single prompt
        prompt = ""
        for msg in conversation:
            role = msg['role']
            content = msg['content']
            prompt += f'<|im_start|>{role}\n{content}<|im_end|>\n'
        assert role == 'user', 'User role is required as the last role.'
        
        before, after = context
        prompt += f'<|im_start|>assistant\n{before}'
        if len(after) == 0:
            after = None
        response = self.openai.completions.create(
            model=self.model,
            prompt=prompt,
            suffix=after,
            temperature=self.temperature,
            max_tokens=self.max_completion_tokens,
            stream=True
        )

        start_time = time.time()
        for chunk in response:
            delta_time = time.time() - start_time
            delta = chunk.choices[0]
            if delta.text is None:
                continue
            yield delta_time, delta.text
            start_time = time.time()
