import pytest
from fastapi.testclient import TestClient
from lima_gui.main import app

client = TestClient(app)


@pytest.fixture(scope="function")
def test_db():
    """Provide a clean test database for each test."""
    # Setup: Use an in-memory SQLite database for testing
    from lima_gui.models.db import get_chat_engine
    import os
    
    # Set environment variable to use a test-specific database
    os.environ["CHAT_DB_URL"] = "sqlite:///:memory:"
    
    # Create all tables
    from lima_gui.models import init_chat
    init_chat()
    
    yield  # Run the test
    
    # Cleanup not necessary for in-memory DB, but good practice
    from sqlalchemy import inspect
    engine = get_chat_engine()
    inspector = inspect(engine)
    for table_name in inspector.get_table_names():
        engine.execute(f"DROP TABLE {table_name}")


def test_create_chat():
    response = client.post("/chats")
    assert response.status_code == 200
    assert 'id' in response.json() and 'name' in response.json()


def test_delete_chat():
    response = client.post("/chats")
    chat_id = response.json()['id']

    response = client.delete(f"/chats/{chat_id}")
    assert response.status_code == 200

    response = client.get(f"/chats")
    ids = []
    for chat_data in response.json():
        ids.append(chat_data['id'])
    assert chat_id not in ids


def test_copy_empty_chat():
    response = client.post("/chats")

    chat_id = response.json()['id']
    chat_name = response.json()['name']

    response = client.post(f"/chats/{chat_id}/copy")
    assert response.status_code == 200
    assert response.json()['name'] == f"{chat_name} - Copy"