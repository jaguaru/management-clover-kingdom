import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import db, get_db
from app.main import create_app
from app.models import Solicitud, Grimorio

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db.Base.metadata.create_all(bind=engine)

app = create_app()


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(scope="module")
def setup_db():
    db.Base.metadata.create_all(bind=engine)
    yield
    db.Base.metadata.drop_all(bind=engine)


def test_create_solicitud(setup_db):
    response = client.post(
        "/api/solicitud/",
        json={
            "nombre": "Juano",
            "apellido": "Perez",
            "identificacion": "123456",
            "edad": 25,
            "afinidad_magica": "Fuego"
        },
    )
    assert response.status_code == 201
    assert response.json()["message"] == "Solicitud added successfully!"


def test_read_solicitudes(setup_db):
    response = client.get("/api/solicitudes/")
    assert response.status_code == 201
    assert "solicitudes" in response.json()


def test_update_solicitud(setup_db):
    response = client.post(
        "/api/solicitud/",
        json={
            "nombre": "Juano",
            "apellido": "Perez",
            "identificacion": "123456d",
            "edad": 25,
            "afinidad_magica": "Fuego",
        },
    )
    print("Mira", response.json())
    solicitud_id = response.json()["solicitud_id"]
    print(solicitud_id, type(solicitud_id))

    response = client.put(
        f"/api/solicitud/{solicitud_id}",
        json={
            "nombre": "Juana",
            "apellido": "Martinez",
            "identificacion": "123456d",
            "edad": 25,
            "afinidad_magica": "Fuego",
        },
    )
    assert response.status_code == 201
    assert response.json()["message"] == "Solicitud updated successfully!"