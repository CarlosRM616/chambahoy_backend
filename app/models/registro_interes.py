# models/registro_interes.py
import uuid

from sqlalchemy import Column, DateTime, ForeignKey, Index, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from sqlalchemy import Enum
from app.models.enums import EstadoInteres

from app.db.database import Base

class RegistroInteres(Base):
    __tablename__ = "registro_interes"

    id_interes = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_usuario = Column(UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=False)
    id_vacante = Column(UUID(as_uuid=True), ForeignKey("vacante.id_vacante"), nullable=False)

    fecha_registro = Column(DateTime(timezone=True), server_default=func.now())
    estado_interes = Column(
        Enum(EstadoInteres, name="estado_interes_enum"),
        nullable=False,
        default=EstadoInteres.pendiente
    )
    fecha_respuesta = Column(DateTime(timezone=True))

    #usuario = relationship("Usuario", back_populates="intereses")
    #vacante = relationship("Vacante", back_populates="intereses")

    __table_args__ = (
        Index(
            "uq_usuario_vacante_activa",
            "id_usuario",
            "id_vacante",
            unique=True,
            postgresql_where=text(
                "estado_interes IN ('pendiente','aceptado')"
            )
        ),
    )