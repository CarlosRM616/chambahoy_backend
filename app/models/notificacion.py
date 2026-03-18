#models/notificacion.py
import uuid
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.db.database import Base


class Notificacion(Base):
    __tablename__ = "notificacion"

    id_notificacion = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_destinatario = Column(UUID(as_uuid=True), nullable=False)
    tipo_notificacion = Column(String(50), nullable=False)
    id_referencia = Column(UUID(as_uuid=True))
    mensaje = Column(String(255), nullable=False)
    leida = Column(Boolean, default=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
