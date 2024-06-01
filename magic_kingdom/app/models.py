from sqlalchemy import Column, Integer, String, Enum
from .database import db


class Solicitud(db.Base):
    """
    Represents a request in the 'solicitudes' table.
    """

    __tablename__ = 'solicitudes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20))
    apellido = Column(String(20))
    identificacion = Column(String(10), unique=True, index=True)
    edad = Column(Integer)
    afinidad_magica = Column(Enum('Oscuridad', 'Luz', 'Fuego', 'Agua', 'Viento', 'Tierra', name='afinidad_magica'))
    estatus = Column(String, default="pendiente")


class Grimorio(db.Base):
    """
    Represents the Grimorio table in the database.
    """

    __tablename__ = "grimorios"

    id = Column(Integer, primary_key=True, index=True)
    tipo_trebol = Column(String, index=True)
    rareza = Column(String, index=True)
    magia = Column(String, index=True)
    escudo = Column(Integer, index=True)
    solicitud_id = Column(Integer, ForeignKey('solicitudes.id'))

    solicitud = relationship("Solicitud", back_populates="grimorios")

Solicitud.grimorios = relationship("Grimorio", back_populates="solicitud")
