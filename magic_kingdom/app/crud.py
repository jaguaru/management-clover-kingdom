from sqlalchemy.orm import Session
from . import models, schema


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
    return db.query(models.Solicitud).filter(models.Solicitud.id == solicitud_id).first()


def update_solicitud(db: Session, solicitud_id: int, solicitud: schema.SolicitudCreate):
    update_db_solicitud = get_solicitud(db, solicitud_id)
    if update_db_solicitud:
        for key, value in solicitud.dict().items():
            setattr(update_db_solicitud, key, value)
        db.commit()
        db.refresh(update_db_solicitud)
    return update_db_solicitud
