from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import crud
import schema
from database import get_db


router = APIRouter()


@router.post("/solicitud/", response_model=schema.Solicitud)
def create_solicitud(solicitud: schema.SolicitudCreate, db: Session = Depends(get_db)):
    """
    Create a new student Solicitud request.
    """

    existing_solicitud = crud.get_solicitud_by_identificacion(
        db=db, 
        identificacion=solicitud.identificacion
    )

    if existing_solicitud:
        return JSONResponse(
            status_code=400,
            content={"message": "The Solicitud with this identification number already exists!"}
        )

    try:
        create_db_solicitud = crud.create_solicitud(db=db, solicitud=solicitud)
        return JSONResponse(
            status_code=201,
            content={
                "message": "Solicitud added successfully!", 
                "solicitud_id": create_db_solicitud.id
            }
        )

    except Exception as _except:
        return JSONResponse(
            status_code=400,
            content={"message": "Could not add this Solicitud!", "error": str(_except)}
        )


@router.put("/solicitud/{solicitud_id}", response_model=schema.Solicitud)
def update_solicitud(solicitud_id: int, solicitud: schema.SolicitudCreate, db: Session = Depends(get_db)):
    """
    Update existing student Solicitud request.
    """

    get_solicitud_by_id = crud.get_solicitud(db, solicitud_id=solicitud_id)

    if get_solicitud_by_id is None:
        return JSONResponse(
            status_code=404,
            content={"message": "Could not find ID Solicitud!"}
        )
    
    try:
        update_db_solicitud = crud.update_solicitud(db=db, solicitud_id=solicitud_id, solicitud=solicitud)
        return JSONResponse(
            status_code=201,
            content={
                "message": "Solicitud updated successfully!", 
                "solicitud_id": update_db_solicitud.id
            }
        )

    except Exception as _except:
        return JSONResponse(
            status_code=400,
            content={"message": "Could not update this Solicitud!", "error": str(_except)}
        )


@router.patch("/solicitud/{solicitud_id}/estatus", response_model=schema.Solicitud)
def update_estado_solicitud(solicitud_id: int, estatus: str, db: Session = Depends(get_db)):
    """
    Update student estatus Solicitud.
    """
    
    get_solicitud_by_id = crud.get_solicitud(db, solicitud_id=solicitud_id)
    
    if get_solicitud_by_id is None:
        return JSONResponse(
            status_code=404,
            content={"message": "Could not find ID Solicitud!"}
        )
    
    try:
        update_status_db_solicitud = crud.update_estatus_solicitud(db=db, solicitud_id=solicitud_id, estatus=estatus)
        return JSONResponse(
            status_code=201,
            content={
                "message": "Estatus updated successfully!", 
                "solicitud_id": update_status_db_solicitud.id
            }
        )

    except Exception as _except:
        return JSONResponse(
            status_code=400,
            content={"message": "Could not update estatus of this Solicitud!", "error": str(_except)}
        )


@router.get("/solicitudes/", response_model=List[schema.Solicitud])
def read_solicitudes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Read existing student Solicitudes.
    """

    try:
        get_all_db_solicitudes = crud.get_solicitudes(db=db, skip=skip, limit=limit)

        if not get_all_db_solicitudes:
            return JSONResponse(
                status_code=404,
                content={"message": "Solicitudes not found!"}
            )
        
        solicitudes_dict = [crud.to_dict(solicitud) for solicitud in get_all_db_solicitudes]

        return JSONResponse(
            status_code=201,
            content={
                "message": "Solicitudes retrieved successfully!", 
                "solicitudes": solicitudes_dict
            }
        )

    except Exception as _except:
        return JSONResponse(
            status_code=500,
            content={"message": "An error occurred while fetching Solicitudes", "error": str(_except)}
        )


@router.get("/asignaciones/", response_model=List[schema.Solicitud])
def read_asignaciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Read existing student Grimorios.
    """

    try:
        get_all_db_solicitudes = crud.get_solicitudes(db=db, skip=skip, limit=limit)
        
        if not get_all_db_solicitudes:
            return JSONResponse(
                status_code=200,
                content={"message": "Asignaciones  not found!"}
            )

        result = []
        for x_solicitud in get_all_db_solicitudes:
            grimorios = crud.get_grimorios_by_solicitud_id(db=db, solicitud_id=x_solicitud.id)
            solicitud_grimorios = {
                "id": x_solicitud.id,
                "identificacion": x_solicitud.identificacion,
                "grimorios": [schema.Grimorio.from_orm(grimorio).dict() for grimorio in grimorios]
            }
            result.append(solicitud_grimorios)
        
        return JSONResponse(
            status_code=200,
            content=result
        )

    except Exception as _except:
        return JSONResponse(
            status_code=500,
            content={"message": "An error occurred while fetching Asignaciones", "error": str(_except)}
        )


@router.delete("/solicitud/{solicitud_id}", response_model=schema.Solicitud)
def delete_solicitud(solicitud_id: int, db: Session = Depends(get_db)):
    """
    Delete existing student Solicitud.
    """

    get_solicitud_by_id = crud.get_solicitud(db, solicitud_id=solicitud_id)
    
    if get_solicitud_by_id is None:
        return JSONResponse(
            status_code=404,
            content={"message": "Could not find ID Solicitud!"}
        )

    try:
        delete_db_solicitud = crud.delete_solicitud(db=db, solicitud_id=solicitud_id)
        return JSONResponse(
            status_code=201,
            content={
                "message": "Solicitud deleted successfully!",
                "solicitud_id": delete_db_solicitud.id
            }
        )

    except Exception as _except:
        return JSONResponse(
            status_code=500,
            content={"message": "Could not delete this Solicitud!", "error": str(_except)}
        )
