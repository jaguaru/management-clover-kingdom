from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import crud, schema
from .database import get_db


router = APIRouter()


@router.post("/solicitud/", response_model=schema.Solicitud)
def create_solicitud(solicitud: schema.SolicitudCreate, db: Session = Depends(get_db)):
    return crud.create_solicitud(db=db, solicitud=solicitud)
