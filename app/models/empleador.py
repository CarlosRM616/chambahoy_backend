#models/empleador.py
import uuid
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.db.database import Base


class Empleador(Base):
    __tablename__ = "empleador"

    id_empleador = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre_visible = Column(String(150), nullable=False)
    correo = Column(String(150), nullable=False, unique=True)
    telefono = Column(String(20))
    contrasena_hash = Column(String(255), nullable=False)
    ubicacion = Column(String(150))
    tipo_empleador = Column(String(30), nullable=False)
    foto_logotipo = Column(String(255))
    fecha_registro = Column(DateTime(timezone=True), server_default=func.now())
    estado_cuenta = Column(String(30), default="activa")
