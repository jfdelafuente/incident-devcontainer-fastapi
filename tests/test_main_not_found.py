# from fastapi.testclient import TestClient
# from api.main import app
# from uuid import uuid4
import pytest
from uuid import uuid4

# filepath: test_main.py

def test_get_aplicacion_not_found(client):
    response = client.get("/aplicacion/error")
    response_json = response.json()
    assert response.status_code == 404
    assert response_json["detail"] == "Aplicacion not found"


def test_update_aplicacion_not_found(client):
    updated_aplicacion = {
        "id": str(uuid4()),
        "nombre": "pangea",
        "descripcion": "updated_description",
        "url": "updated@correo.com",
        "marca": "updated_marca",
        "dominio": "updated_dominio",
        "responsable": "updated_responsable",
        "first_nivel": [],
        "second_nivel": [],
        "tercer_nivel": [],
        "coordinador": [],
        "horario_servicio": "24x7",
        "horario_atencion": "24x7",
        "ventana_intervencion": "24x7",
        "ventana_intervencion_semanal": "24x7",
        "ventana_intervencion_mensual": "24x7",
        "observaciones": "updated_observaciones",
        "centro_afectado": "updated_centro_afectado",
        "impacto_negocio": "updated_impacto_negocio"
    }
    response = client.put("/aplicacion/error", json=updated_aplicacion)
    response_json = response.json()
    assert response.status_code == 404
    assert response_json["detail"] == "Aplicacion not found"

def test_delete_aplicacion_not_found(client):
    response = client.delete("/aplicacion/error")
    response_json = response.json()
    assert response.status_code == 404
    assert response_json["detail"] == "Aplicacion not found"