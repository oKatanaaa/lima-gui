from copy import deepcopy

from .function import Function


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
            "tags": [],
            "functions": []
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
    def last_msg(self):
        if len(self.chat["dialog"]) == 0:
            return None
        return self.chat["dialog"][-1]
        
    @property
    def last_role(self):
        if len(self.chat["dialog"]) == 0:
            return None
        return self.chat["dialog"][-1]["role"]
    
    @property
    def tags(self):
        return self.chat["tags"]
    
    @property
    def functions(self):
        out = []
        for fn_dict in self.chat["functions"]:
            out.append(Function(deepcopy(fn_dict)))
        return out
        
    def __len__(self):
        return len(self.chat["dialog"])
    
    def add_msg(self, role, content):
        msg = {"role": role, "content": content}
        # It is assummed that previous message contains a function call.
        if role == 'function':
            msg["name"] = self.chat["dialog"][-1]["function_call"]["name"]
        self.chat["dialog"].append(msg)
    
    def edit_msg(self, ind, role, content, function_call_data=None):
        print(ind, role, content, function_call_data)
        msg = {"role": role, "content": content}
        if function_call_data is not None:
            msg["function_call"] = function_call_data
        
        # It is assummed that previous message contains a function call.
        if role == 'function':
            msg["name"] = self.chat["dialog"][ind - 1]["function_call"]["name"]
        self.chat["dialog"][ind] = msg
    
    def remove_msg(self, ind):
        self.chat["dialog"].pop(ind)
        
    def add_fn(self, fn_obj: Function):
        self.chat["functions"].append(fn_obj.fn_dict)
    
    def edit_fn(self, ind, fn_obj: Function):
        self.chat["functions"][ind] = fn_obj.fn_dict
    
    def remove_fn(self, ind):
        self.chat["functions"].pop(ind)
        
    def get_fn(self, ind):
        return Function(deepcopy(self.chat["functions"][ind]))
        
    def add_tag(self, tag):
        if tag not in self.chat["tags"]:
            self.chat["tags"].append(tag)
    
    def remove_tag(self, tag):
        self.chat["tags"].remove(tag)
        
    def get_conversation_history(self, ind):
        return deepcopy(self.chat["dialog"][:ind])

    def to_str(self):
        return '\n'.join([msg['content'] for msg in self.chat['dialog']])
    
    def __repr__(self):
        return str(self.chat)

