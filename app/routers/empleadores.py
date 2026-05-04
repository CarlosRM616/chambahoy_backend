#routers/empleadores.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.empleador import Empleador
from app.schemas.empleador import EmpleadorCreate, EmpleadorResponse

router = APIRouter(
    prefix="/empleadores",
    tags=["Empleadores"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# routers/empleadores.py
@router.post("/", response_model=EmpleadorResponse)
def crear_empleador(
    empleador: EmpleadorCreate,
    db: Session = Depends(get_db)
):
    nuevo_empleador = Empleador(
        nombre_visible=empleador.nombre_visible,
        correo=empleador.correo,
        telefono=empleador.telefono,
        ubicacion=empleador.ubicacion,
        tipo_empleador=empleador.tipo_empleador,
        foto_logotipo=empleador.foto_logotipo,
        contrasena_hash=empleador.contrasena
    )
    db.add(nuevo_empleador)
    db.commit()
    db.refresh(nuevo_empleador)
    return nuevo_empleador


@router.get("/", response_model=list[EmpleadorResponse])
def listar_empleadores(db: Session = Depends(get_db)):
    return db.query(Empleador).all()
