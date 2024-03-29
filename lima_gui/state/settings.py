from tokenizers import Tokenizer


class Settings:
    instance = None
    
    DEFAULT_TAGS = [
        'conversational',
        'functional',
        'summarization',
        'classification',
        'translation',
        'paraphrasing',
        'text continuation',
        'text infilling',
        'text enhancement',
        'creative text generation',
        'world qa',
        'contextual qa',
        'logic',
        'coding',
        'meta problems',
        'agent'
    ]
    DEFAULT_TOKENIZER = 'mistralai/Mistral-7B-v0.1'
    
    @staticmethod
    def get_instance():
        if Settings.instance is None:
            Settings.instance = Settings(Settings.DEFAULT_TAGS, Settings.DEFAULT_TOKENIZER)
        return Settings.instance
    
    def __init__(self, tags: list, tokenizer_name: str, languages: list = ['en', 'ru']):
        assert Settings.instance is None, 'Settings instance already exists. Please use get_instance method.'
        self.tags = tags
        self.languages = languages
        self.set_tokenizer(tokenizer_name)
        
    def set_tokenizer(self, tokenizer_name: str):
        self.tokenizer_name = tokenizer_name
        self.tokenizer = Tokenizer.from_pretrained(tokenizer_name)
        
    def get_token_count(self, str):
        return len(self.tokenizer.encode(str))
