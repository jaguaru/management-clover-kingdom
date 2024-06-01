from pydantic import BaseModel, Field, constr, validator
from enum import Enum


class AfinidadMagica(str, Enum):
    oscuridad = 'Oscuridad'
    luz = 'Luz'
    fuego = 'Fuego'
    agua = 'Agua'
    viento = 'Viento'
    tierra = 'Tierra'


class SolicitudBase(BaseModel):
    nombre: str
    apellido: str
    identificacion: constr(max_length=10)
    edad: int = Field(..., ge=10, le=99)
    afinidad_magica: AfinidadMagica

    @validator('nombre', 'apellido')
    def name_must_be_letters(cls, str_value):
        assert str_value.isalpha(), 'must contain only letters'
        assert 5 <= len(str_value) <= 20, 'must be between 5 and 20 characters'
        return str_value


class SolicitudCreate(SolicitudBase):
    pass


class Solicitud(SolicitudBase):
    id: int
    estatus: str

    class Config:
        orm_mode = True
