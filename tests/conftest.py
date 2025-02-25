import pytest

from api.main import app as api_app
from fastapi.testclient import TestClient

@pytest.fixture()
def app():
    app = api_app
    return app

@pytest.fixture()
def client():
    client = TestClient(api_app)
    yield client