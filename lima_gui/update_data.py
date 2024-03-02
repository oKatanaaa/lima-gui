import argparse
import pandas as pd
import json
import os
from glob import glob

from lima_gui.model import Chat
from lima_gui.model import ChatDataset


OLD_NEW_KEYS_MAPPING = {
    'tags': Chat.KEY_TAGS,
    'name': Chat.KEY_NAME,
    'dialog': Chat.KEY_MESSAGES,
    'functions': Chat.KEY_TOOLS,
    'lang': Chat.KEY_LANGUAGE
}

def _remap(chat):
    for old_key, new_key in OLD_NEW_KEYS_MAPPING.items():
        chat[new_key] = chat.get(old_key, Chat.DEFAULT_VALS[new_key])
        
    for old_key in set(OLD_NEW_KEYS_MAPPING.keys()) - set(OLD_NEW_KEYS_MAPPING.values()):
        if old_key in chat:
            del chat[old_key]


def update(read_path, write_path):
    df = pd.read_csv(read_path)
    chats = []
    for chat_str in df["chat"]:
        chat = json.loads(chat_str)
        _remap(chat)
        chats.append(chat)
    dataset = ChatDataset(chats)
    dataset.save_jsonl(write_path)


def main(input_path, output_path):
    if os.path.isdir(input_path) and os.path.isdir(output_path):
        for input_file in glob(os.path.join(input_path, '*.csv')):
            output_file = os.path.join(output_path, os.path.basename(input_file))
            output_file = output_file.replace('.csv', '.jsonl')
            update(input_file, output_file)
    elif os.path.isfile(input_path) and os.path.isfile(output_path): 
        update(input_path, output_path)
    else:
        raise ValueError(f'Input and output paths must be either directories or files,' \
                         ' but received input_path={input_path} and output_path={output_path}') 
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Lima GUI chat data from old format to new format.')
    parser.add_argument('input', type=str, help='Input directory or file path')
    parser.add_argument('output', type=str, help='Output directory or file path')

    args = parser.parse_args()

    main(args.input, args.output)

