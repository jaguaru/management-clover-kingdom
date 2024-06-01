from fastapi import FastAPI
import uvicorn
from app.student_endpoints import router as solicitud_router


app = FastAPI()

app.include_router(solicitud_router, prefix="/api")


if __name__ == "__main__":
    """
    This block ensures that the script runs only when executed directly,
    not when imported as a module
    """
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
