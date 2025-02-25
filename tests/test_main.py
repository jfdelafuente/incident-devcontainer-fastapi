from fastapi.testclient import TestClient
from api.main import app
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

def test_create_aplicacion(client):
    new_aplicacion = {
        "id": str(uuid4()),
        "nombre": "new_app",
        "descripcion": "new_description",
        "url": "new_app@correo.com",
        "marca": "new_marca",
        "dominio": "new_dominio",
        "responsable": "new_responsable",
        "first_nivel": [],
        "second_nivel": [],
        "tercer_nivel": [],
        "coordinador": [],
        "horario_servicio": "24x7",
        "horario_atencion": "24x7",
        "ventana_intervencion": "24x7",
        "ventana_intervencion_semanal": "24x7",
        "ventana_intervencion_mensual": "24x7",
        "observaciones": "new_observaciones",
        "centro_afectado": "new_centro_afectado",
        "impacto_negocio": "new_impacto_negocio"
    }
    response = client.post("/aplicacion/", json=new_aplicacion)
    assert response.status_code == 200
    assert response.json()["nombre"] == "new_app"

def test_update_soporte(client):
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
    response = client.put("/aplicacion/pangea", json=updated_aplicacion)
    assert response.status_code == 200
    assert response.json()["descripcion"] == "updated_description"

def test_delete_book(client):
    response = client.delete("/soporte/pangea")
    assert response.status_code == 200
    assert response.json()["message"] == "Aplicacion deleted successfully"
