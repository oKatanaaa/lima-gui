
class Chat:
    @staticmethod
    def create_empty():
        return Chat({
            "name": "New Chat",
            "lang": "en",
            "dialog": []
        })
        
    def __init__(self, chat: dict):
        """
        Parameters
        ----------
        chats : dict
            {
                "name": chatname,
                "lang": lang,
                "dialog": [{"role": role, "content": content}]
            }
        """
        self.chat = chat
    
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
        
    def __len__(self):
        return len(self.chat["dialog"])
    
    def add_msg(self, role, content):
        self.chat["dialog"].append({"role": role, "content": content})
    
    def edit_msg(self, ind, role, content):
        self.chat["dialog"][ind] = {"role": role, "content": content}
    
    def remove_msg(self, ind):
        self.chat["dialog"].pop(ind)