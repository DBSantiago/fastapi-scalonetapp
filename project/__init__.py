from fastapi import FastAPI, APIRouter

from .database import SessionLocal, engine
from . import models
from .routers import router_roles
from .routers import router_equipos
from .routers import router_selecciones
from .routers import router_integrantes
from .routers import router_usuarios

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API - La ScalonetApp",
    description="API para el proyecto La ScalonetApp. Nos permite realizar operaciones CRUD sobre selecciones y sus "
                "integrantes.",
    version="1")

api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(router_roles)
api_v1.include_router(router_equipos)
api_v1.include_router(router_selecciones)
api_v1.include_router(router_integrantes)
api_v1.include_router(router_usuarios)

app.include_router(api_v1)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
