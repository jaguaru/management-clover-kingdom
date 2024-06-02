import pytest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from app import crud, schema, models

@pytest.fixture
def mock_db_session():
    return MagicMock(spec=Session)

def test_get_solicitud_by_identificacion(mock_db_session):
    mock_identificacion = "123456"
    mock_solicitud = models.Solicitud(
        id=1, nombre="Juan", apellido="Perez", identificacion=mock_identificacion, edad=25, afinidad_magica="Fuego"
    )
    mock_db_session.query.return_value.filter.return_value.first.return_value = mock_solicitud

    result = crud.get_solicitud_by_identificacion(mock_db_session, mock_identificacion)

    assert result == mock_solicitud
    

def test_create_solicitud(mock_db_session):
    solicitud_data = schema.SolicitudCreate(
        nombre="Juano", apellido="Perez", identificacion="123456", edad=25, afinidad_magica="Fuego"
    )
    created_solicitud = models.Solicitud(id=1, **solicitud_data.dict())
    mock_db_session.add.side_effect = lambda x: x
    mock_db_session.commit.side_effect = None
    mock_db_session.refresh.side_effect = lambda x: None

    mock_assign_grimorio = MagicMock()
    crud.assign_grimorio = mock_assign_grimorio

    result = crud.create_solicitud(mock_db_session, solicitud_data)

    assert result.nombre == solicitud_data.nombre
    assert result.apellido == solicitud_data.apellido
    assert result.identificacion == solicitud_data.identificacion
    assert result.edad == solicitud_data.edad
    assert result.afinidad_magica == solicitud_data.afinidad_magica
    mock_db_session.add.assert_called_once_with(result)
    mock_db_session.commit.assert_called_once()
    mock_db_session.refresh.assert_called_once_with(result)
    mock_assign_grimorio.assert_called_once_with(mock_db_session, result.id)
