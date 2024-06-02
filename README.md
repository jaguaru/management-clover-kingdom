# Management Clover Kingdom

Welcome to the Clover Kingdom Magic Requests repository, a platform designed to efficiently manage all magic-related requests in our kingdom.

In order to use all the features of this application you must have all the necessary packages installed. In the application installation part you will find the instructions to install everything.


# Firt steps:


### Dowload the repository:

Open a window console and type

    $ git clone https://github.com/jaguaru/management-clover-kingdom.git

## Setting up the virtual environment:

Open the management-clover-kingdom directory:

    $ cd management-clover-kingdom

Create the directory for the virtual environment:

    $ mkdir venv

Create the virtual environment:

    $ python3 -m venv venv

Activate the virtual environment:

    $ source venv/bin/activate

Virtual environment activated:

    (venv) $

Install the required packages:

    (venv) $ pip install -r requirements.txt

Run the FastAPI server:

    (venv) $ uvicorn main:app --reload


# View project documentation with FastAPI Swagger

Write this address in the address bar of the browser. 

    URL: http://127.0.0.1:8000/docs

To use this option you must have followed the previous instructions


# Interacting with the REST API

This REST API consists of two sections, the first is for user authentication and the second is for managing tickets and uploading images to the cloud.

The first step is to get an application, such as Postman or another similar application, to make local and remote http requests and get a response.


### Create Solicitud: 

Send the student's application for admission.

    Request:

    URL: http://127.0.0.1:8000/api/solicitud/
    Header: Content-Type: application/json
    Method: POST
    Body:

        {
            "nombre": "Nikola",
            "apellido": "Tesla",
            "identificacion": "ABCD7070",
            "edad": 54,
            "afinidad_magica": "Luz"
        }

    Response:

        {
            "message":"Solicitud added successfully!",
            "solicitud_id": 28
        }

### Update Solicitud: 

Updates the student's entry application. The necessary data must be changed in the BODY.

    Request:

    URL: http://127.0.0.1:8000/api/solicitud/{solicitud_id}/
    Header: Content-Type: application/json
    Method: PUT
    Body:

        {
            "nombre": "Nikola",
            "apellido": "Tesla",
            "identificacion": "ABCD7071",
            "edad": 62,
            "afinidad_magica": "Luz"
        }

    Response:

        {
            "message":"Solicitud updated successfully!",
            "solicitud_id": 28
        }

### Update Estatus Solicitud: 

Updates the status of the student's request.

    Request:

    URL: http://127.0.0.1:8000/api/solicitud/{solicitud_id}/estatus?estatus=aprobado
    Header: Content-Type: application/json
    Method: PATCH
    Body:

    Response:

        {
            "message":"Solicitudes retrieved successfully!",
            "solicitud_id": 28
        }

### Read Solicitudes: 

View all student requests.

    Request:

    URL: http://127.0.0.1:8000/api/solicitudes/?skip=0&limit=100
    Header: Content-Type: application/json
    Method: GET
    Body:

    Response:

        {
            "message":"Solicitudes retrieved successfully!",
            "solicitudes": [{
                                "id":28,
                                "nombre":"Nikola","apellido":"Tesla","identificacion":"ABCD7071","edad":71,
                                "afinidad_magica":"Luz","estatus":"aprobado"
                            }]
        }

### Read Asignaciones: 

Check the Grimorios assignments that each student has.

    Request:

    URL: http://127.0.0.1:8000/api/asignaciones/?skip=0&limit=100
    Header: Content-Type: application/json
    Method: GET
    Body:

    Response:

        {
            "id": 28,
            "identificacion": ABCD7071,
            "grimorios": [
                            {
                                "id":27,
                                "identificacion":"ABCD7011",
                                "grimorios":[{
                                                "tipo_trebol":"5 hojas",
                                                "rareza":"extra epico",
                                                "magia":"legendaria",
                                                "escudo":100,"id":5,
                                                "solicitud_id":27
                                            }]
                            },
                            {
                                "id":28,
                                "identificacion":"ABCD7071",
                                "grimorios":[{
                                                "tipo_trebol":"3 hojas",
                                                "rareza":"inusual",
                                                "magia":"intermedia",
                                                "escudo":50,
                                                "id":6,
                                                "solicitud_id":28
                                            }]
                            }
                         ]
        }

### Read Asignaciones: 

Check the Grimorios assignments that each student has.

    Request:

    URL: http://127.0.0.1:8000/api/solicitud/{solicitud_id}
    Header: Content-Type: application/json
    Method: DELETE
    Body:

    Response:

        {
            "message":"Solicitud deleted successfully!",
            "solicitud_id": 28
        }

# Create Docker image

Open the management-clover-kingdom directory:

    $ cd management-clover-kingdom

Create the container image

    $ docker build -t magic-kingdom .

Activate the container

    $ docker run -it -p 4000:8000 magic_kingdom

# Activate Docker-compose

Open the management-clover-kingdom directory:

    $ cd management-clover-kingdom

Build and start the services

    $ docker-compose up --build

Stopping the services

    $ docker-compose down

