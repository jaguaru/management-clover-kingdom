from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from . import crud, schema
from .database import get_db


router = APIRouter()


@router.post("/solicitud/", response_model=schema.Solicitud)
def create_solicitud(solicitud: schema.SolicitudCreate, db: Session = Depends(get_db)):
    """
    Create a new student application request.
    """

    existing_solicitud = crud.get_solicitud_by_identificacion(
        db=db, 
        identificacion=solicitud.identificacion
    )

    if existing_solicitud:
        return JSONResponse(
            status_code=400,
            content={"message": "The request with this identification number already exists!"}
        )

    try:
        db_solicitud = crud.create_solicitud(db=db, solicitud=solicitud)
        return JSONResponse(
            status_code=201,
            content={
                "message": "Request added successfully!", 
                "identificacion": db_solicitud.identificacion
            }
        )

    except Exception as _except:
        return JSONResponse(
            status_code=400,
            content={"message": "Could not add this request!", "error": _except}
        )
