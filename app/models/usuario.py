#models/usuario.py
import uuid
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.db.database import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(100), nullable=False)
    apellido_paterno = Column(String(100), nullable=False)
    apellido_materno = Column(String(100))
    telefono = Column(String(20), nullable=False, unique=True)
    correo = Column(String(150), nullable=False, unique=True)
    contrasena_hash = Column(String(255), nullable=False)
    ubicacion = Column(String(150))
    disponibilidad = Column(Boolean, default=True)
    tipo_usuario = Column(String(30), default="buscador_empleo")
    foto_perfil = Column(String(255))
    fecha_registro = Column(DateTime(timezone=True), server_default=func.now())
    estado_cuenta = Column(String(30), default="activa")
