CREATE DATABASE magic_kingdom_db;

CREATE TYPE MAGIC AS ENUM ('Oscuridad', 'Luz', 'Fuego', 'Agua', 'Viento', 'Tierra');
CREATE TABLE solicitudes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(20),
    apellido VARCHAR(20),
    identificacion VARCHAR(10) UNIQUE,
    edad INTEGER,
    afinidad_magica MAGIC,
    estatus VARCHAR DEFAULT 'pendiente'
);


CREATE TABLE grimorios (
    id SERIAL PRIMARY KEY,
    tipo_trebol VARCHAR(20),
    rareza VARCHAR(20),
    magia VARCHAR(20),
    escudo INTEGER,
    solicitud_id INTEGER,
    FOREIGN KEY (solicitud_id) REFERENCES solicitudes (id)
);
