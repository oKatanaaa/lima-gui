from copy import deepcopy
import json
from typing import List

from .function import Function
from .role import Role


class Chat:
    KEY_NAME = 'name'
    KEY_TOOLS = 'tools'
    KEY_MESSAGES = 'messages'
    KEY_LANGUAGE = 'lang'
    KEY_TAGS = 'tags'
    
    DEFAULT_NAME = 'New chat'
    DEFAULT_LANG = 'en'
    DEFAULT_TAGS = []
    DEFAULT_VALS = {
        KEY_NAME: DEFAULT_NAME,
        KEY_LANGUAGE: DEFAULT_LANG,
        KEY_MESSAGES: [],
        KEY_TAGS: DEFAULT_TAGS,
        KEY_TOOLS: []
    }
    
    @staticmethod
    def create_empty():
        return Chat(deepcopy(Chat.DEFAULT_VALS))
        
    def __init__(self, chat: dict):
        """
        Parameters
        ----------
        chats : dict
            {
                "name": chatname,
                "lang": lang,
                "tags":  { tag1, tag2, ... } # it is a set, so it is unique
                "messages": [{"role": role, "content": content}]
                "tools": [...]
            }
        """
        self.chat = chat
        for k, v in Chat.DEFAULT_VALS.items():
            if k not in self.chat:
                self.chat[k] = v

    @property
    def name(self):
        return self.chat[Chat.KEY_NAME]
    
    @name.setter
    def name(self, name):
        self.chat[Chat.KEY_NAME] = name[:64]
        
    @property
    def language(self):
        return self.chat[Chat.KEY_LANGUAGE]
    
    @language.setter
    def language(self, lang):
        assert lang in ['en', 'ru']
        self.chat[Chat.KEY_LANGUAGE] = lang
    
    @property
    def last_msg(self):
        if len(self.chat[Chat.KEY_MESSAGES]) == 0:
            return None
        return self.chat[Chat.KEY_MESSAGES][-1]
        
    @property
    def last_role(self):
        if len(self.chat[Chat.KEY_MESSAGES]) == 0:
            return None
        return self.chat[Chat.KEY_MESSAGES][-1]["role"]
    
    @property
    def tags(self):
        return self.chat[Chat.KEY_TAGS]
    
    @property
    def functions(self) -> List[Function]:
        out = []
        for fn_dict in self.chat[Chat.KEY_TOOLS]:
            out.append(Function(deepcopy(fn_dict)))
        return out
        
    def __len__(self):
        return len(self.chat[Chat.KEY_MESSAGES])
    
    def add_msg(self, role, content):
        msg = {"role": role, "content": content}
        # It is assummed that previous message contains a function call.
        if role == Role.FUNCTION:
            msg["name"] = self.chat[Chat.KEY_MESSAGES][-1]["function_call"]["name"]
        self.chat[Chat.KEY_MESSAGES].append(msg)
    
    def edit_msg(self, ind, role, content, function_call_data=None):
        msg = {"role": role, "content": content}
        if function_call_data is not None and role == 'assistant':
            msg["function_call"] = function_call_data
        
        # It is assummed that previous message contains a function call.
        if role == Role.FUNCTION:
            msg["name"] = self.chat[Chat.KEY_MESSAGES][ind - 1]["function_call"]["name"]
        self.chat[Chat.KEY_MESSAGES][ind] = msg
    
    def remove_msg(self, ind):
        self.chat[Chat.KEY_MESSAGES].pop(ind)
        
    def add_fn(self, fn_obj: Function):
        self.chat[Chat.KEY_TOOLS].append(fn_obj.fn_dict)
    
    def edit_fn(self, ind, fn_obj: Function):
        self.chat[Chat.KEY_TOOLS][ind] = fn_obj.fn_dict
    
    def remove_fn(self, ind):
        self.chat[Chat.KEY_TOOLS].pop(ind)
        
    def get_fn(self, ind):
        return Function(deepcopy(self.chat[Chat.KEY_TOOLS][ind]))
        
    def add_tag(self, tag):
        if tag not in self.chat[Chat.KEY_TAGS]:
            self.chat[Chat.KEY_TAGS].append(tag)
    
    def remove_tag(self, tag):
        self.chat[Chat.KEY_TAGS].remove(tag)
        
    def get_conversation_history(self, ind):
        return deepcopy(self.chat[Chat.KEY_MESSAGES][:ind])

    def to_str(self):
        output_str = ""
        if len(self.chat[Chat.KEY_TOOLS]) > 0:
            output_str += "Functions:\n"
            for fn in self.functions:
                output_str += f"{json.dumps(fn.to_openai_dict())}\n"
                
        for msg in self.chat[Chat.KEY_MESSAGES]:
            if 'function_call' in msg:
                output_str += f"{msg['role']}: {msg['content']} <{msg['function_call']['name']}>\n"
            else:
                output_str += f"{msg['role']}: {msg['content']}\n"
        return output_str
    
    def to_openai_dict(self):
        d = {'messages': self.chat[Chat.KEY_MESSAGES]}
        if len(self.functions) > 0:
            functions = []
            for fn in self.functions:
                functions.append(fn.to_openai_dict())
            d['tools'] = functions
        return d
    
    def __repr__(self):
        return str(self.chat)
