# In services/file_service.py
from typing import Optional
from sqlalchemy.orm import Session
from lima_gui.models import Chat, Message, Tool, ToolCall, Tag
import json


class FileService:
    def __init__(self, db: Session):
        self.db = db
    
    def import_jsonl(self, file_path: str) -> int:
        """Import chats from a JSONL file and add to database."""
        chats_added = 0
        
        with open(file_path, 'r') as f:
            for line in f:
                chat_data = json.loads(line)
                # Convert from file format to database models
                chat = Chat(name=chat_data.get("name", "Imported Chat"), language=chat_data.get("lang", "en"))
                
                # Add tags
                for tag_name in chat_data.get("tags", []):
                    tag = self.db.query(Tag).filter(Tag.name == tag_name).first()
                    if not tag:
                        tag = Tag(name=tag_name)
                        self.db.add(tag)
                    chat.tags.append(tag)
                
                # Add messages
                for i, msg_data in enumerate(chat_data.get("messages", [])):
                    message = Message(
                        role=msg_data["role"],
                        content=msg_data.get("content", ""),
                        position=i
                    )
                    
                    # Handle function calls if present
                    if "function_call" in msg_data:
                        tool_call = ToolCall(
                            name=msg_data["function_call"]["name"],
                            arguments=json.dumps(msg_data["function_call"].get("arguments", {}))
                        )
                        message.tool_calls.append(tool_call)
                    
                    chat.messages.append(message)
                
                # Add tools
                for tool_data in chat_data.get("tools", []):
                    tool = Tool(
                        name=tool_data["function"]["name"],
                        description=tool_data["function"].get("description", ""),
                        parameters=tool_data["function"].get("parameters", {})
                    )
                    chat.tools.append(tool)
                
                self.db.add(chat)
                chats_added += 1
                
        self.db.commit()
        return chats_added
    
    def export_jsonl(self, file_path: str) -> int:
        """Export all chats from database to a JSONL file."""
        chats = self.db.query(Chat).all()
        
        with open(file_path, 'w') as f:
            for chat in chats:
                # Convert to file format
                chat_data = {
                    "name": chat.name,
                    "lang": chat.language,
                    "tags": [tag.name for tag in chat.tags],
                    "messages": [],
                    "tools": []
                }
                
                # Add messages
                for message in sorted(chat.messages, key=lambda m: m.position):
                    msg_data = {
                        "role": message.role,
                        "content": message.content
                    }
                    
                    # Add function call if present
                    if message.tool_calls:
                        tool_call = message.tool_calls[0]  # Assuming one tool call per message
                        msg_data["function_call"] = {
                            "name": tool_call.name,
                            "arguments": json.loads(tool_call.arguments) if tool_call.arguments else {}
                        }
                    
                    chat_data["messages"].append(msg_data)
                
                # Add tools
                for tool in chat.tools:
                    tool_data = {
                        "type": "function",
                        "function": {
                            "name": tool.name,
                            "description": tool.description,
                            "parameters": tool.parameters
                        }
                    }
                    chat_data["tools"].append(tool_data)
                
                f.write(json.dumps(chat_data) + "\n")
            
        return len(chats)