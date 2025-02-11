from fastapi import FastAPI
from mangum import Mangum  # For ASGI compatibility on Vercel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Vercel"}

handler = Mangum(app)  # Required for Vercel to handle FastAPI
