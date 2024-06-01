import random
from sqlalchemy.orm import Session
from . import models, schema


def to_dict(obj):
    """
    Converts a SQLAlchemy object to a dictionary.
    """
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}


def get_solicitud_by_identificacion(db: Session, identificacion: str):
    """Get a solicitud by its identificacion."""
    return db.query(models.Solicitud).filter(models.Solicitud.identificacion == identificacion).first()


def create_solicitud(db: Session, solicitud: schema.SolicitudCreate):
    """Create a new solicitud in the database."""
    create_db_solicitud = models.Solicitud(**solicitud.dict())
    db.add(create_db_solicitud)
    db.commit()
    db.refresh(create_db_solicitud)

    assign_grimorio(db, create_db_solicitud.id)

    return create_db_solicitud


def create_grimorio(db: Session, grimorio: schema.GrimorioCreate, solicitud_id: int):
    create_db_grimorio = models.Grimorio(**grimorio.dict(), solicitud_id=solicitud_id)
    db.add(create_db_grimorio)
    db.commit()
    db.refresh(create_db_grimorio)
    return create_db_grimorio


def assign_grimorio(db: Session, solicitud_id: int):
    """
    Assigns a Grimorio to a Solicitud based on Escudo rarity.
    """

    grimorios = [
        {"tipo_trebol": "1 hoja", "rareza": "comun", "magia": "normal", "escudo": 7},
        {"tipo_trebol": "2 hojas", "rareza": "raro", "magia": "bsica", "escudo": 28},
        {"tipo_trebol": "3 hojas", "rareza": "inusual", "magia": "intermedia", "escudo": 50},
        {"tipo_trebol": "4 hojas", "rareza": "super inusual", "magia": "avanzada", "escudo": 84},
        {"tipo_trebol": "5 hojas", "rareza": "extra epico", "magia": "legendaria", "escudo": 100},
    ]

    types = [g["tipo_trebol"] for g in grimorios]
    shields = [g["escudo"] for g in grimorios]

    selected_type = random.choices(types, weights=shields, k=1)[0]

    selected_grimorio = next(filter(lambda g: g["tipo_trebol"] == selected_type, grimorios))

    grimorio_data = schemas.GrimorioCreate(
        tipo_trebol=selected_grimorio["tipo_trebol"],
        rareza=selected_grimorio["rareza"],
        magia=selected_grimorio["magia"],
        escudo=selected_grimorio["escudo"]
    )

    return create_grimorio(db=db, grimorio=grimorio_data, solicitud_id=solicitud_id)


def get_solicitud(db: Session, solicitud_id: int):
    """Get a solicitud by its ID."""
    return db.query(models.Solicitud).filter(models.Solicitud.id == solicitud_id).first()


def get_solicitudes(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of Solicitudes from the database with optional pagination.
    """
    return db.query(models.Solicitud).offset(skip).limit(limit).all()


def get_grimorios_by_solicitud_id(db: Session, solicitud_id: int):
    """
    Retrieve a list of Grimorios from the database with optional pagination.
    """
    return db.query(models.Grimorio).filter(models.Grimorio.solicitud_id == solicitud_id).all()


def update_solicitud(db: Session, solicitud_id: int, solicitud: schema.SolicitudCreate):
    """Update an existing solicitud in the database."""
    update_db_solicitud = get_solicitud(db, solicitud_id)
    if update_db_solicitud:
        for key, value in solicitud.dict().items():
            setattr(update_db_solicitud, key, value)
        db.commit()
        db.refresh(update_db_solicitud)
    return update_db_solicitud


def update_estatus_solicitud(db: Session, solicitud_id: int, estatus: str):
    """Update the status of an existing solicitud in the database."""
    update_status_db_solicitud = get_solicitud(db, solicitud_id)
    if update_status_db_solicitud:
        update_status_db_solicitud.estatus = estatus
        db.commit()
        db.refresh(update_status_db_solicitud)
    return update_status_db_solicitud


def delete_solicitud(db: Session, solicitud_id: int):
    """
    Deletes a student Solicitud from the database.
    """
    delete_db_solicitud = get_solicitud(db, solicitud_id)
    if delete_db_solicitud:
        db.delete(delete_db_solicitud)
        db.commit()
    return delete_db_solicitud
