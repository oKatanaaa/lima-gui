import json
import os
import tempfile

import pytest
from fastapi.testclient import TestClient
from lima_gui.main import app


client = TestClient(app)


@pytest.fixture(scope="function")
def test_db():
    """Provide a clean test database for each test."""
    from lima_gui.models import init_chat
    from lima_gui.models import db as db_module

    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    os.environ["CHAT_DB_URL"] = f"sqlite:///{path}"

    if db_module._chat_engine is not None:
        db_module._chat_engine.dispose()
    db_module._chat_engine = None
    db_module._chat_session = None

    init_chat()

    try:
        yield
    finally:
        if db_module._chat_session is not None:
            db_module._chat_session.remove()
            db_module._chat_session = None
        if db_module._chat_engine is not None:
            db_module._chat_engine.dispose()
            db_module._chat_engine = None
        os.environ.pop("CHAT_DB_URL", None)
        if os.path.exists(path):
            os.remove(path)


def test_create_chat(test_db):
    response = client.post("/chats")
    assert response.status_code == 200
    assert 'id' in response.json() and 'name' in response.json()


def test_delete_chat(test_db):
    response = client.post("/chats")
    chat_id = response.json()['id']

    response = client.delete(f"/chats/{chat_id}")
    assert response.status_code == 200

    response = client.get(f"/chats")
    ids = []
    for chat_data in response.json():
        ids.append(chat_data['id'])
    assert chat_id not in ids


def test_copy_empty_chat(test_db):
    response = client.post("/chats")

    chat_id = response.json()['id']
    chat_name = response.json()['name']

    response = client.post(f"/chats/{chat_id}/copy")
    assert response.status_code == 200
    assert response.json()['name'] == f"{chat_name} - Copy"


def test_copy_chat_preserves_metadata(test_db):
    create_resp = client.post("/chats")
    chat_id = create_resp.json()["id"]

    update_payload = {"language": "fr", "tags": ["alpha", "beta"]}
    assert client.put(f"/chat/{chat_id}", json=update_payload).status_code == 200

    tool_payload = {
        "name": "calculator",
        "description": "Simple math",
        "parameters": {"type": "object", "properties": {"a": {"type": "number"}}},
    }
    tool_resp = client.post(f"/chat/{chat_id}/tools", json=tool_payload)
    assert tool_resp.status_code == 200

    message_resp = client.post(f"/chat/{chat_id}/message")
    message_id = message_resp.json()["id"]
    assert client.put(
        f"/chat/{chat_id}/message/{message_id}",
        json={"content": "Solve", "role": "user"},
    ).status_code == 200

    tool_call_payload = {"name": "calculator", "arguments": json.dumps({"a": 2, "b": 3})}
    assert (
        client.post(
            f"/chat/{chat_id}/message/{message_id}/tool_call",
            json=tool_call_payload,
        ).status_code
        == 200
    )

    copy_resp = client.post(f"/chats/{chat_id}/copy")
    assert copy_resp.status_code == 200
    copy_id = copy_resp.json()["id"]

    copied_chat = client.get(f"/chat/{copy_id}").json()
    assert copied_chat["language"] == "fr"
    assert copied_chat["tags"] == ["alpha", "beta"]
    assert copied_chat["tools"] == [tool_payload]
    assert copied_chat["messages"][0]["content"] == "Solve"
    assert copied_chat["messages"][0]["role"] == "user"
    assert copied_chat["messages"][0]["tool_calls"] == [
        {"id": copied_chat["messages"][0]["tool_calls"][0]["id"], "tool_name": "calculator"}
    ]


def test_upload_chat_preserves_metadata(test_db):
    chat_payload = {
        "name": "Uploaded Chat",
        "language": "de",
        "tags": ["imported"],
        "tools": [
            {
                "name": "search",
                "description": "Lookup",
                "parameters": {"type": "object", "properties": {"query": {"type": "string"}}},
            }
        ],
        "messages": [
            {
                "role": "assistant",
                "content": "Here is the info",
                "tool_calls": [{"name": "search", "arguments": "{\"query\": \"info\"}"}],
            }
        ],
    }

    jsonl_content = json.dumps(chat_payload) + "\n"

    response = client.post(
        "/chats/upload",
        files={
            "file": ("import.jsonl", jsonl_content.encode("utf-8"), "application/jsonl"),
        },
    )
    assert response.status_code == 200

    chats = client.get("/chats").json()
    imported_chat = next(chat for chat in chats if chat["name"] == "Uploaded Chat")
    assert imported_chat["language"] == "de"
    assert imported_chat["tags"] == ["imported"]
    assert imported_chat["tools"][0]["name"] == "search"

    detail = client.get(f"/chat/{imported_chat['id']}").json()
    assert detail["messages"][0]["role"] == "assistant"
    assert detail["messages"][0]["tool_calls"] == [
        {"id": detail["messages"][0]["tool_calls"][0]["id"], "tool_name": "search"}
    ]
