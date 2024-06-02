import unittest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from app.main import app
from app.crud import get_solicitud_by_identificacion, create_solicitud, get_solicitud, update_solicitud, delete_solicitud
from app.database import get_db
from app.schema import Solicitud, SolicitudCreate

client = TestClient(app)

class TestStudentEndpoints(unittest.TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        app.dependency_overrides[get_db] = lambda: self.mock_db

    def tearDown(self):
        app.dependency_overrides = {}

    def test_create_solicitud(self):
        self.mock_db.get_solicitud_by_identificacion.return_value = None
        self.mock_db.create_solicitud.return_value = Solicitud(id=1, identificacion="123456789")

        response = client.post("/api/solicitud/", json={"identificacion": "123456789"})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            "message": "Solicitud added successfully!",
            "solicitud_id": 1
        })