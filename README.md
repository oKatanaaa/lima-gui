# LIMA-GUI

LIMA-GUI is a simple utility for gathering LIMA-like data to train you own LLM (like LLAMA, MPT or others).

It uses a simple data format that closely resembles OpenAI API. Chat is represented as a list of JSONs:
```json
[
    {
        "role": "role",
        "content": "content"
    }
]
```

Example chat:
```json
[
    {
        "role": "user",
        "content": "Hey, what is 4 + 4?"
    },
    {
        "role": "assistant",
        "content": "Hey! 4 + 4 is 8."
    }
]
```

## Usage

1. First install the lima-gui by running `pip install -e .` in the repo folder.
2. Run `python -m lima_gui.app`

## TODO

- [ ] Safeguards not to lose data.
- [ ] Message indices.
- [ ] Somehow refactor current shitty chat UI.
    - [x] Make scrolling smooth.
    - [x] Make list items fit message contents.
    - [ ] Scrolling at the end of the list.
    - [ ] Select/Focus newly added item.
- [ ] Huggingface integration (download and upload).
- [x] Token count using Huggingface tokenizers (LLAMA tokenizer by default).
- [ ] Manual on how to use lima-gui.
- [x] Tags for chats (like coding, logic, qa, etc).
- [x] Default dataset config (contains config for languages, tags and tokenizer).