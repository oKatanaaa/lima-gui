import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from lima_gui.main import app
from lima_gui.models.chat import ChatBase, Chat, Tag
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


def create_chat(session_factory, *, name="Chat", language="en", tags=None):
    with session_factory() as session:
        tag_objects = []
        if tags:
            for tag_name in tags:
                tag = session.get(Tag, tag_name)
                if not tag:
                    tag = Tag(name=tag_name)
                    session.add(tag)
                tag_objects.append(tag)

        chat = Chat(name=name, language=language)
        chat.tags = tag_objects
        session.add(chat)
        session.commit()
        session.refresh(chat)
        return chat.id


def test_update_chat_name_only(client_and_session):
    client, session_factory = client_and_session
    chat_id = create_chat(session_factory, name="Original")

    response = client.put(f"/chat/{chat_id}", json={"name": "Updated"})

    assert response.status_code == 200

    with session_factory() as session:
        updated_chat = session.get(Chat, chat_id)
        assert updated_chat.name == "Updated"


def test_update_chat_language_only(client_and_session):
    client, session_factory = client_and_session
    chat_id = create_chat(session_factory, language="en")

    response = client.put(f"/chat/{chat_id}", json={"language": "fr"})

    assert response.status_code == 200

    with session_factory() as session:
        updated_chat = session.get(Chat, chat_id)
        assert updated_chat.language == "fr"


def test_update_chat_tags_with_strings(client_and_session):
    client, session_factory = client_and_session
    chat_id = create_chat(session_factory, tags=["initial"])

    response = client.put(f"/chat/{chat_id}", json={"tags": ["alpha", "beta"]})

    assert response.status_code == 200

    with session_factory() as session:
        updated_chat = session.get(Chat, chat_id)
        assert sorted(tag.name for tag in updated_chat.tags) == ["alpha", "beta"]
        all_tags = session.query(Tag).filter(Tag.name.in_(["alpha", "beta"])).all()
        assert sorted(tag.name for tag in all_tags) == ["alpha", "beta"]
