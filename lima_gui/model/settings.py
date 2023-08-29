from transformers import AutoTokenizer


class Settings:
    instance = None
    
    DEFAULT_TAGS = [
        'summarization',
        'classification',
        'translation',
        'paraphrasing',
        'text continuation',
        'text infilling',
        'text enhancement',
        'question answering',
        'logic',
        'coding',
        'meta problems'
    ]
    DEFAULT_TOKENIZER = 'meta-llama/Llama-2-7b-hf'
    
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
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        
    def get_token_count(self, str):
        return len(self.tokenizer.tokenize(str))
