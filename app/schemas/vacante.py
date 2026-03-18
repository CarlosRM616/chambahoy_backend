# schemas/vacante.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional


class VacanteBase(BaseModel):
    titulo: str
    descripcion: str
    ubicacion: str
    sueldo: Optional[float] = None
    tipo_contrato: Optional[str] = None
    horario: Optional[str] = None

    lunes: bool = False
    martes: bool = False
    miercoles: bool = False
    jueves: bool = False
    viernes: bool = False
    sabado: bool = False
    domingo: bool = False

    edad_requerida: Optional[str] = None
    sexo_requerido: Optional[str] = None
    habilidades_requeridas: Optional[str] = None
    aceptacion_automatica: bool = False


class VacanteCreate(VacanteBase):
    id_empleador: UUID


class VacanteResponse(VacanteBase):
    id_vacante: UUID
    id_empleador: UUID
    estado_vacante: str
    fecha_publicacion: datetime
    fecha_cierre: datetime

    class Config:
        from_attributes = True
