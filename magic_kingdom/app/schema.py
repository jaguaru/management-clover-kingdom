from pydantic import BaseModel, Field, constr
from enum import Enum


class AfinidadMagica(str, Enum):
    oscuridad = 'Oscuridad'
    luz = 'Luz'
    fuego = 'Fuego'
    agua = 'Agua'
    viento = 'Viento'
    tierra = 'Tierra'


class SolicitudBase(BaseModel):
    nombre: constr(max_length=20)
    apellido: constr(max_length=20)
    identificacion: constr(max_length=10)
    edad: int = Field(..., ge=10, le=99)
    afinidad_magica: AfinidadMagica


class SolicitudCreate(SolicitudBase):
    pass


class Solicitud(SolicitudBase):
    id: int
    estatus: str

    class Config:
        orm_mode = True
