from pydantic import BaseModel, Field, constr, validator
from enum import Enum


class AfinidadMagica(str, Enum):
    oscuridad = 'Oscuridad'
    luz = 'Luz'
    fuego = 'Fuego'
    agua = 'Agua'
    viento = 'Viento'
    tierra = 'Tierra'


class GrimorioBase(BaseModel):
    tipo_trebol: str
    rareza: str
    magia: str
    escudo: int


class GrimorioCreate(GrimorioBase):
    pass


class Grimorio(GrimorioBase):
    id: int
    solicitud_id: int

    class Config:
        orm_mode = True


class SolicitudBase(BaseModel):
    nombre: str
    apellido: str
    identificacion: str
    edad: int
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

    @validator('edad')
    def edad_must_be_two_digits(cls, int_value):
        assert isinstance(int_value, int) and 5 <= int_value <= 99, 'must be a valid age (5-99)'
        return int_value


class SolicitudCreate(SolicitudBase):
    pass


class Solicitud(SolicitudBase):
    id: int
    estatus: str

    class Config:
        orm_mode = True
        from_attributes = True
