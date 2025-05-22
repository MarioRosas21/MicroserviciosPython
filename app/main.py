from fastapi import FastAPI
from app.routers import usuarios, productos

app = FastAPI()

app.include_router(usuarios.router)
app.include_router(productos.router)