# schemas/registro_interes.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID


class RegistroInteresCreate(BaseModel):
    id_usuario: UUID
    id_vacante: UUID


class RegistroInteresResponse(BaseModel):
    id_interes: UUID
    id_usuario: UUID
    id_vacante: UUID
    estado_interes: str
    fecha_registro: datetime
    fecha_respuesta: Optional[datetime] = None

    class Config:
        from_attributes = True
