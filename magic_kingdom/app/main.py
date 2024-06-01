from fastapi import FastAPI
import uvicorn


app = FastAPI()


if __name__ == "__main__":
    """
    This block ensures that the script runs only when executed directly,
    not when imported as a module
    """
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
