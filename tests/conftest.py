import pytest

from api.main import app as api_app
from fastapi.testclient import TestClient
from uuid import uuid4


@pytest.fixture()
def app_id():
    """Generate a random app id"""
    return str(uuid4())

@pytest.fixture()
def app_nombre():
    """Generate a random app nombre"""
    return str(uuid4())

@pytest.fixture()
def app_payload(app_id):
    """Generate an app payload"""
    return {
        "id": app_id,
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

@pytest.fixture()
def app_payload_update(app_id):
    """Generate an app payload"""
    return {
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


@pytest.fixture()
def app_payload_wrong(app_id):
    """Generate an app payload"""
    return {
        "id": str(uuid4()),
        "nombre": 6,  # aquí está el error, debe ser string
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

@pytest.fixture()
def app():
    app = api_app
    return app

@pytest.fixture()
def client():
    client = TestClient(api_app)
    yield client