from sqlalchemy.orm import Session
from . import models, schema


def to_dict(obj):
    """
    Converts a SQLAlchemy object to a dictionary.
    """
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}


def get_solicitud_by_identificacion(db: Session, identificacion: str):
    """Get a solicitud by its identificacion."""
    return db.query(models.Solicitud).filter(models.Solicitud.identificacion == identificacion).first()


def create_solicitud(db: Session, solicitud: schema.SolicitudCreate):
    """Create a new solicitud in the database."""
    create_db_solicitud = models.Solicitud(**solicitud.dict())
    db.add(create_db_solicitud)
    db.commit()
    db.refresh(create_db_solicitud)
    return create_db_solicitud


def get_solicitud(db: Session, solicitud_id: int):
    """Get a solicitud by its ID."""
    return db.query(models.Solicitud).filter(models.Solicitud.id == solicitud_id).first()


def get_solicitudes(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of Solicitudes from the database with optional pagination.
    """
    return db.query(models.Solicitud).offset(skip).limit(limit).all()


def update_solicitud(db: Session, solicitud_id: int, solicitud: schema.SolicitudCreate):
    """Update an existing solicitud in the database."""
    update_db_solicitud = get_solicitud(db, solicitud_id)
    if update_db_solicitud:
        for key, value in solicitud.dict().items():
            setattr(update_db_solicitud, key, value)
        db.commit()
        db.refresh(update_db_solicitud)
    return update_db_solicitud


def update_estatus_solicitud(db: Session, solicitud_id: int, estatus: str):
    """Update the status of an existing solicitud in the database."""
    update_status_db_solicitud = get_solicitud(db, solicitud_id)
    if update_status_db_solicitud:
        update_status_db_solicitud.estatus = estatus
        db.commit()
        db.refresh(update_status_db_solicitud)
    return update_status_db_solicitud
