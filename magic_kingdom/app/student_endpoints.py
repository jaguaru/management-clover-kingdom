from fastapi import APIRouter
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db


router = APIRouter()


@router.post("/solicitud/", response_model=schemas.Solicitud)
def create_solicitud(solicitud: schemas.SolicitudCreate, db: Session = Depends(get_db)):
    return crud.create_solicitud(db=db, solicitud=solicitud)
