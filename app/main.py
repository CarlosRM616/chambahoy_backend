#app/main.py
from fastapi import FastAPI

from app.db.database import engine, Base

from app.models.usuario import Usuario
from app.models.empleador import Empleador
from app.models.vacante import Vacante
from app.models.registro_interes import RegistroInteres
from app.models.notificacion import Notificacion

from app.routers import usuarios
from app.routers import empleadores
from app.routers import vacantes
from app.routers import registro_interes

app = FastAPI(
    title="ChambaHoy API",
    description="Backend del MVP de empleos urgentes ChambaHoy",
    version="0.1.0"
)

app.include_router(usuarios.router)
app.include_router(empleadores.router)
app.include_router(vacantes.router)
app.include_router(registro_interes.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"mensaje": "ChambaHoy backend activo"}
