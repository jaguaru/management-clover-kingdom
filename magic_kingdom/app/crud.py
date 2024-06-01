from sqlalchemy.orm import Session
from . import models, schema


def get_solicitud_by_identificacion(db: Session, identificacion: str):
    return db.query(models.Solicitud).filter(models.Solicitud.identificacion == identificacion).first()


def create_solicitud(db: Session, solicitud: schema.SolicitudCreate):
    db_solicitud = models.Solicitud(**solicitud.dict())
    db.add(db_solicitud)
    db.commit()
    db.refresh(db_solicitud)
    return db_solicitud

def update_solicitud(db: Session, solicitud_id: int, solicitud: schema.SolicitudCreate):
    update_db_solicitud = get_solicitud(db, solicitud_id)
    if update_db_solicitud:
        for key, value in solicitud.dict().items():
            setattr(db_solicitud, key, value)
        db.commit()
        db.refresh(db_solicitud)
    return db_solicitud
