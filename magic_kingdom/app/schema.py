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
    identificacion: str
    edad: int = Field(..., ge=10, le=99)
    afinidad_magica: AfinidadMagica

    @validator('nombre', 'apellido')
    def name_must_be_letters(cls, str_value):
        assert str_value.isalpha(), 'must contain only letters'
        assert 5 <= len(str_value) <= 20, 'must be between 5 and 20 characters'
        return str_value

    @validator('identificacion')
    def identificacion_must_be_alphanumeric(cls, id_value):
        assert id_value.isalnum(), 'must contain only letters and numbers'
        assert 5 <= len(id_value) <= 10, 'must be between 5 and 10 characters or less'
        return id_value


class SolicitudCreate(SolicitudBase):
    pass


class Solicitud(SolicitudBase):
    id: int
    estatus: str

    class Config:
        orm_mode = True
