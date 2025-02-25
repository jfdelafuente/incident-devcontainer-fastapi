# from fastapi.testclient import TestClient
# from api.main import app
# from uuid import uuid4
import pytest
from uuid import uuid4

# filepath: test_main.py


def test_get_aplicacion_not_found(client, app_nombre):
    response = client.get(f"/aplicacion/{app_nombre}")
    response_json = response.json()
    assert response.status_code == 404
    assert response_json["detail"] == "Aplicacion not found"


def test_update_aplicacion_not_found(client, app_nombre, app_payload_update):
    response = client.put(f"/aplicacion/{app_nombre}", json=app_payload_update)
    response_json = response.json()
    assert response.status_code == 404
    assert response_json["detail"] == "Aplicacion not found"


def test_delete_aplicacion_not_found(client, app_nombre):
    response = client.delete(f"/aplicacion/{app_nombre}")
    response_json = response.json()
    assert response.status_code == 404
    assert response_json["detail"] == "Aplicacion not found"


def test_create_aplicacion_wrong_payload(client):
    response = client.post("/aplicacion/", json={})
    assert response.status_code == 422
    # assert response.json()["nombre"] == "new_app"


def test_update_aplicacion_wrong_payload(client, app_payload_wrong):
    response = client.put("/aplicacion/pangea", json=app_payload_wrong)
    response_json = response.json()
    print(response_json)
    assert response.status_code == 422
    assert response_json == {
        'detail': [
            {
                'type': 'string_type',
                'loc': ['body', 'nombre'],
                'msg': 'Input should be a valid string',
                'input': 6
            }
        ]
    }
