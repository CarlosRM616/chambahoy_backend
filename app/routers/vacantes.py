# routers/vacantes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.db.database import SessionLocal
from app.models.vacante import Vacante
from app.schemas.vacante import VacanteCreate, VacanteResponse


router = APIRouter(
    prefix="/vacantes",
    tags=["Vacantes"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=VacanteResponse)
def crear_vacante(vacante: VacanteCreate, db: Session = Depends(get_db)):
    nueva_vacante = Vacante(
        id_empleador=vacante.id_empleador,
        titulo=vacante.titulo,
        descripcion=vacante.descripcion,
        ubicacion=vacante.ubicacion,
        sueldo=vacante.sueldo,
        tipo_contrato=vacante.tipo_contrato,
        horario=vacante.horario,

        lunes=vacante.lunes,
        martes=vacante.martes,
        miercoles=vacante.miercoles,
        jueves=vacante.jueves,
        viernes=vacante.viernes,
        sabado=vacante.sabado,
        domingo=vacante.domingo,

        edad_requerida=vacante.edad_requerida,
        sexo_requerido=vacante.sexo_requerido,
        habilidades_requeridas=vacante.habilidades_requeridas,

        fecha_cierre=datetime.utcnow() + timedelta(days=7),
        aceptacion_automatica=vacante.aceptacion_automatica
    )

    db.add(nueva_vacante)
    db.commit()
    db.refresh(nueva_vacante)
    return nueva_vacante


@router.get("/", response_model=list[VacanteResponse])
def listar_vacantes(db: Session = Depends(get_db)):
    return db.query(Vacante).filter(Vacante.estado_vacante == "activa").all()
