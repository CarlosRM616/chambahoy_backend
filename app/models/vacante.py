# models/vacante.py

import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import String, DateTime, Boolean, Text, DECIMAL, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.db.database import Base


class Vacante(Base):
    __tablename__ = "vacante"

    id_vacante: Mapped[uuid.UUID] = mapped_column( UUID(as_uuid=True), primary_key=True, default=uuid.uuid4 )
    id_empleador: Mapped[uuid.UUID] = mapped_column( UUID(as_uuid=True), ForeignKey("empleador.id_empleador"), nullable=False )

    titulo: Mapped[str] = mapped_column(String(150), nullable=False)
    descripcion: Mapped[str] = mapped_column(Text, nullable=False)
    ubicacion: Mapped[str] = mapped_column(String(150), nullable=False)

    sueldo: Mapped[Decimal | None] = mapped_column(DECIMAL(10, 2))
    tipo_contrato: Mapped[str | None] = mapped_column(String(30))
    horario: Mapped[str | None] = mapped_column(String(100))

    lunes: Mapped[bool] = mapped_column(Boolean, default=False)
    martes: Mapped[bool] = mapped_column(Boolean, default=False)
    miercoles: Mapped[bool] = mapped_column(Boolean, default=False)
    jueves: Mapped[bool] = mapped_column(Boolean, default=False)
    viernes: Mapped[bool] = mapped_column(Boolean, default=False)
    sabado: Mapped[bool] = mapped_column(Boolean, default=False)
    domingo: Mapped[bool] = mapped_column(Boolean, default=False)

    edad_requerida: Mapped[str | None] = mapped_column(String(50))
    sexo_requerido: Mapped[str | None] = mapped_column(String(30))
    habilidades_requeridas: Mapped[str | None] = mapped_column(Text)

    estado_vacante: Mapped[str] = mapped_column(String(30), default="activa")
    fecha_publicacion: Mapped[datetime] = mapped_column( DateTime(timezone=True), server_default=func.now() )
    fecha_cierre: Mapped[datetime] = mapped_column( DateTime(timezone=True), nullable=False )
    aceptacion_automatica: Mapped[bool] = mapped_column(Boolean, default=False)
