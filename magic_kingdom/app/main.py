from fastapi import FastAPI
import uvicorn
from student_endpoints import router as solicitud_router


def create_app():
    """
    This function creates and configures the FastAPI application.
    """
    app = FastAPI()
    app.include_router(solicitud_router, prefix="/api")
    return app

app = create_app()


if __name__ == "__main__":
    """
    This block ensures that the script runs only when executed directly,
    not when imported as a module.
    """
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
