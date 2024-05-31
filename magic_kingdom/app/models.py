from sqlalchemy import Column, Integer, String, Enum
from database import db


# Model definition for the 'solicitudes' table
class Solicitud(db.Base):
    
    __tablename__ = 'solicitudes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20))
    apellido = Column(String(20))
    identificacion = Column(String(10), unique=True, index=True)
    edad = Column(Integer)
    afinidad_magica = Column(Enum('Oscuridad', 'Luz', 'Fuego', 'Agua', 'Viento', 'Tierra', name='afinidad_magica'))
    estatus = Column(String, default="pendiente")
