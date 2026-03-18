# schemas/usuario.py
from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional


class UsuarioBase(BaseModel):
    nombre: str
    apellido_paterno: str
    apellido_materno: Optional[str] = None
    correo: EmailStr
    telefono: str
    ubicacion: Optional[str] = None
    disponibilidad: bool = True
    foto_perfil: Optional[str] = None


class UsuarioCreate(UsuarioBase):
    contrasena: str


class UsuarioResponse(UsuarioBase):
    id_usuario: UUID
    tipo_usuario: str
    estado_cuenta: str
    fecha_registro: datetime

    class Config:
        from_attributes = True
