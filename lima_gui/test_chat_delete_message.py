import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from lima_gui.main import app
from lima_gui.models.chat import ChatBase, Chat, Message, RoleEnum
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


def create_chat_with_messages(session_factory):
    with session_factory() as session:
        chat = Chat(name="Chat", language="en")
        session.add(chat)
        session.flush()

        message_ids = []
        for index, content in enumerate(["first", "second", "third"], start=1):
            message = Message(
                chat=chat,
                role=RoleEnum.user,
                content=content,
                position=index,
            )
            session.add(message)
            session.flush()
            message_ids.append(message.id)

        session.commit()
        return chat.id, message_ids


def test_delete_message_reorders_remaining_positions(client_and_session):
    client, session_factory = client_and_session
    chat_id, message_ids = create_chat_with_messages(session_factory)

    response = client.delete(f"/chat/{chat_id}/message/{message_ids[1]}")

    assert response.status_code == 200

    with session_factory() as session:
        remaining = (
            session.query(Message)
            .filter(Message.chat_id == chat_id)
            .order_by(Message.position)
            .all()
        )
        assert [message.id for message in remaining] == [message_ids[0], message_ids[2]]
        assert [message.position for message in remaining] == [1, 2]
