from enum import Enum

class EstadoInteres(str, Enum):
    pendiente = "pendiente"
    aceptado = "aceptado"
    rechazado = "rechazado"
    expirado = "expirado"
    bloqueado = "bloqueado"