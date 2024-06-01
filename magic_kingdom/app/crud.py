from sqlalchemy import Session
from . import models, schema


def create_solicitud(db: Session, solicitud: schemas.SolicitudCreate):
    db_solicitud = models.Solicitud(**solicitud.dict())
    db.add(db_solicitud)
    db.commit()
    db.refresh(db_solicitud)
    return db_solicitud
