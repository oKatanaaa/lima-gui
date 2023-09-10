
class Chat:
    DEFAULT_NAME = 'CHAT'
    DEFAULT_LANG = 'en'
    DEFAULT_TAGS = []
    DEFAULT_VALS = {
        'name': DEFAULT_NAME,
        'lang': DEFAULT_LANG,
        'dialog': [],
        'tags': DEFAULT_TAGS
    }
    
    @staticmethod
    def create_empty():
        return Chat({
            "name": "New Chat",
            "lang": "en",
            "dialog": [],
            "tags": []
        })
        
    def __init__(self, chat: dict):
        """
        Parameters
        ----------
        chats : dict
            {
                "name": chatname,
                "lang": lang,
                "tags":  { tag1, tag2, ... } # it is a set, so it is unique
                "dialog": [{"role": role, "content": content}]
            }
        """
        self.chat = chat
        for k, v in Chat.DEFAULT_VALS.items():
            if k not in self.chat:
                self.chat[k] = v

    @property
    def name(self):
        return self.chat["name"]
    
    @name.setter
    def name(self, name):
        self.chat["name"] = name[:64]
        
    @property
    def language(self):
        return self.chat["lang"]
    
    @language.setter
    def language(self, lang):
        assert lang in ['en', 'ru']
        self.chat["lang"] = lang
        
    @property
    def last_role(self):
        if len(self.chat["dialog"]) == 0:
            return None
        return self.chat["dialog"][-1]["role"]
    
    @property
    def tags(self):
        return self.chat["tags"]
        
    def __len__(self):
        return len(self.chat["dialog"])
    
    def add_msg(self, role, content):
        self.chat["dialog"].append({"role": role, "content": content})
    
    def edit_msg(self, ind, role, content):
        self.chat["dialog"][ind] = {"role": role, "content": content}
    
    def remove_msg(self, ind):
        self.chat["dialog"].pop(ind)
    
    def add_tag(self, tag):
        if tag not in self.chat["tags"]:
            self.chat["tags"].append(tag)
    
    def remove_tag(self, tag):
        self.chat["tags"].remove(tag)
        
    def get_conversation_history(self, ind):
        return self.chat["dialog"][:ind]

    def to_str(self):
        return '\n'.join([msg['content'] for msg in self.chat['dialog']])
