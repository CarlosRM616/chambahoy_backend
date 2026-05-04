from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app.db.database import SessionLocal
from app.models.registro_interes import RegistroInteres
from app.models.vacante import Vacante
from app.models.empleador import Empleador
from app.schemas.registro_interes import (
    RegistroInteresCreate,
    RegistroInteresResponse
)

router = APIRouter(
    prefix="/registro-interes",
    tags=["RegistroInteres"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def validar_vacante_activa(vacante: Vacante):
    if vacante is None:
        raise HTTPException(status_code=404, detail="Vacante no encontrada")

    if vacante.estado_vacante != "activa":
        raise HTTPException(status_code=400, detail="La vacante no está activa")

    ahora = datetime.now(timezone.utc)

    if vacante.fecha_cierre is not None and vacante.fecha_cierre <= ahora:
        raise HTTPException(status_code=400, detail="La vacante ya venció")
    
    
def validar_interes_unico(db: Session, id_usuario, id_vacante):
    interes_existente = db.query(RegistroInteres).filter(
        RegistroInteres.id_usuario == id_usuario,
        RegistroInteres.id_vacante == id_vacante
    ).first()

    if interes_existente:
        raise HTTPException(
            status_code=400,
            detail="Ya registraste interés en esta vacante"
        )


def determinar_estado(vacante: Vacante, db: Session):
    if vacante.aceptacion_automatica:
        return "aceptado", datetime.now(timezone.utc)

    return "pendiente", None


@router.post("/", response_model=RegistroInteresResponse)
def registrar_interes(
    datos: RegistroInteresCreate,
    db: Session = Depends(get_db)
):
    # 1. Buscar vacante
    vacante = db.query(Vacante).filter(
        Vacante.id_vacante == datos.id_vacante
    ).first()

    # 2. Validar vacante
    validar_vacante_activa(vacante)

    # 3. Validar interés único
    validar_interes_unico(db, datos.id_usuario, datos.id_vacante)

    # 4. Determinar estado
    estado, fecha_respuesta = determinar_estado(vacante, db)

    # 5. Crear registro
    nuevo_interes = RegistroInteres(
        id_usuario=datos.id_usuario,
        id_vacante=datos.id_vacante,
        estado_interes=estado,
        fecha_respuesta=fecha_respuesta
    )

    db.add(nuevo_interes)
    db.commit()
    db.refresh(nuevo_interes)

    return nuevo_interes
