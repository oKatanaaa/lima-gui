import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from lima_gui.main import app
from lima_gui.models.chat import ChatBase, Chat, Message, Tag, Tool, RoleEnum
from lima_gui.models.db import get_chat_db


@pytest.fixture()
def client_and_session():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    ChatBase.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(bind=engine)

    def override_get_chat_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_chat_db] = override_get_chat_db

    with TestClient(app) as test_client:
        yield test_client, TestingSessionLocal

    app.dependency_overrides.pop(get_chat_db, None)


def seed_chat(session_factory):
    with session_factory() as session:
        tag_alpha = session.get(Tag, "alpha")
        if not tag_alpha:
            tag_alpha = Tag(name="alpha")
            session.add(tag_alpha)
        tool = Tool(
            name="calculator",
            description="Performs arithmetic",
            parameters={"type": "object", "properties": {"a": {"type": "number"}}},
        )
        chat = Chat(name="Metadata", language="fr")
        chat.tags.append(tag_alpha)
        chat.tools.append(tool)
        chat.messages.append(
            Message(
                role=RoleEnum.system,
                content="bonjour monde",
                position=1,
            )
        )
        chat.messages.append(
            Message(
                role=RoleEnum.assistant,
                content="salut",
                position=2,
            )
        )
        session.add(chat)
        session.commit()
        session.refresh(chat)
        chat_id = chat.id

    return chat_id


def test_chat_details_include_metadata(client_and_session):
    client, session_factory = client_and_session
    chat_id = seed_chat(session_factory)

    response = client.get(f"/chat/{chat_id}")
    assert response.status_code == 200

    payload = response.json()
    assert payload["language"] == "fr"
    assert payload["tags"] == ["alpha"]
    assert payload["tools"] == [
        {
            "name": "calculator",
            "description": "Performs arithmetic",
            "parameters": {"type": "object", "properties": {"a": {"type": "number"}}},
        }
    ]
    # Token calculation splits on whitespace, so the two messages yield three tokens total.
    assert payload["tokens"] == 3
    assert payload["n_msgs"] == 2


def test_chat_list_contains_metadata(client_and_session):
    client, session_factory = client_and_session
    chat_id = seed_chat(session_factory)

    response = client.get("/chats")
    assert response.status_code == 200

    chat_list = response.json()
    assert isinstance(chat_list, list)
    chat_entry = next(item for item in chat_list if item["id"] == chat_id)
    assert chat_entry["language"] == "fr"
    assert chat_entry["tags"] == ["alpha"]
    assert chat_entry["tokens"] == 3
    assert chat_entry["message_count"] == 2
    assert chat_entry["tools"] == [
        {
            "name": "calculator",
            "description": "Performs arithmetic",
            "parameters": {"type": "object", "properties": {"a": {"type": "number"}}},
        }
    ]
