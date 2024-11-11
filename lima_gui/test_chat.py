# import pytest
# from fastapi.testclient import TestClient
# from lima_gui.main import app
# from dotenv import load_dotenv

# load_dotenv(".env.test")

# client = TestClient(app)

# def test_create_chat():
#     response = client.post("/chats")
#     assert response.status_code == 200
#     assert 'id' in response.json() and 'name' in response.json()

# def test_delete_chat():
#     response = client.post("/chats")
#     chat_id = response.json()['id']

#     response = client.delete(f"/chats/{chat_id}")
#     assert response.status_code == 200

#     response = client.get(f"/chats")
#     ids = []
#     for chat_data in response.json():
#         ids.append(chat_data['id'])
#     assert chat_id not in ids

# def test_copy_empty_chat():
#     response = client.post("/chats")

#     chat_id = response.json()['id']
#     chat_name = response.json()['name']

#     response = client.post(f"/chats/{chat_id}/copy")
#     assert response.status_code == 200
#     assert response.json()['name'] == f"{chat_name} - Copy"