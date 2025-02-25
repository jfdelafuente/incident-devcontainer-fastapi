from fastapi.testclient import TestClient
# from api.main import app
from uuid import uuid4

# filepath: test_main.py

# client = TestClient(app)

def test_get_all_aplicaciones(client):
    response = client.get("/aplicaciones")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_aplicacion(client):
    response = client.get("/aplicacion/pangea")
    assert response.status_code == 200
    assert response.json()["nombre"] == "pangea"

def test_create_aplicacion(client, app_payload):
    response = client.post("/aplicacion/", json=app_payload)
    assert response.status_code == 200
    assert response.json()["nombre"] == "new_app"

def test_update_aplicacion(client, app_payload_update):
    response = client.put("/aplicacion/pangea", json=app_payload_update)
    assert response.status_code == 200
    assert response.json()["descripcion"] == "updated_description"
    assert response.json()["nombre"] == "pangea"

def test_delete_aplicacion(client):
    response = client.delete("/aplicacion/pangea")
    assert response.status_code == 200
    assert response.json()["message"] == "Aplicacion deleted successfully"
