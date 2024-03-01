import json
import pandas as pd
from typing import List, Dict, Any, Union

from .chat import Chat
from .function import Function


class ChatDataset:
    def __init__(self, chats: List[Dict[str, Any]]):
        """
        Parameters
        ----------
        chats : List[Dict[str, Any]]
            [{
                "name": chatname,
                "lang": lang,
                "tags": { tag1, tag2, ... }, # it is a set
                "dialog": [{"role": role, "content": content}]
            }]
        """
        self._chats = chats
        
    def __len__(self):
        return len(self._chats)
    
    @property
    def chats(self) -> List[Chat]:
        chats = []
        for chat in self._chats:
            chats.append(Chat(chat))
        return chats
        
    def get_chat(self, ind):
        return Chat(self._chats[ind])
    
    def remove_chat(self, ind):
        self._chats.pop(ind)
    
    def add_chat(self, chat: Union[Dict[str, Any], Chat]):
        if isinstance(chat, Chat):
            chat = chat.chat
        self._chats.append(chat)
    
    def to_pandas(self) -> pd.DataFrame:
        data = []
        for chat in self._chats:
            chat_str = json.dumps(chat)
            data.append(chat_str)
        
        return pd.DataFrame(data, columns=["chat"])
    
    def __hash__(self) -> int:
        global_repr = ""
        for chat in self._chats:
            chat_str = json.dumps(chat)
            global_repr += chat_str
        return hash(global_repr)
    
    def save_csv(self, path):
        if not path.endswith(".csv"):
            path += ".csv"
        pd = self.to_pandas()
        pd.to_csv(path, index=False)
    
    def save_openai_jsonl(self, path):
        if not path.endswith(".jsonl"):
            path += ".jsonl"
        with open(path, "w") as f:
            for chat in self.chats:
                chat_str = json.dumps(chat.to_openai_dict())
                f.write(chat_str + "\n")
    
    def save_jsonl(self, path):
        if not path.endswith(".jsonl"):
            path += ".jsonl"
        with open(path, "w") as f:
            for chat in self._chats:
                chat_str = json.dumps(chat)
                f.write(chat_str + "\n")
    
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
    
    @staticmethod
    def from_jsonl(filename) -> 'ChatDataset':
        chats = []
        with open(filename, "r") as f:
            for line in f.readlines():
                chat = json.loads(line)
                chats.append(chat)
        return ChatDataset(chats)

    