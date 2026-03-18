# schemas/empleador.py
from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional


class EmpleadorBase(BaseModel):
    nombre_visible: str
    correo: EmailStr
    telefono: Optional[str] = None
    ubicacion: Optional[str] = None
    tipo_empleador: str
    foto_logotipo: Optional[str] = None


class EmpleadorCreate(EmpleadorBase):
    contrasena: str


class EmpleadorResponse(EmpleadorBase):
    id_empleador: UUID
    estado_cuenta: str
    fecha_registro: datetime

    class Config:
        from_attributes = True
