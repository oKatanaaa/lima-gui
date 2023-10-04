import json
import pandas as pd
from typing import List, Dict, Any, Union

from .chat import Chat


class ChatDataset:
    def __init__(self, chats: List[Dict[str, Any]]):
        """
        Parameters
        ----------
        chats : List[Dict[str, Any]]
            [{
                "system_prompt": str,
                "chat": [{
                    "name": chatname,
                    "lang": lang,
                    "tags": { tag1, tag2, ... }, # it is a set
                    "dialog": [{"role": role, "content": content}]
            }]
        """
        self.chats = chats
        
    def __len__(self):
        return len(self.chats)
        
    def get_chat(self, ind):
        return Chat(self.chats[ind])
    
    def remove_chat(self, ind):
        self.chats.pop(ind)
    
    def add_chat(self, chat: Union[Dict[str, Any], Chat]):
        if isinstance(chat, Chat):
            chat = chat.chat
        self.chats.append(chat)
    
    def to_pandas(self) -> pd.DataFrame:
        data = []
        for chat in self.chats:
            chat_str = json.dumps(chat)
            data.append(chat_str)
        
        return pd.DataFrame(data, columns=["chat"])
    
    @staticmethod
    def from_pandas(df: pd.DataFrame) -> 'ChatDataset':
        chats = []
        for chat_str in df["chat"]:
            chat = json.loads(chat_str)
            chats.append(chat)
        return ChatDataset(chats)
    
    @staticmethod
    def from_csv(filename) -> 'ChatDataset':
        return ChatDataset.from_pandas(pd.read_csv(filename))
