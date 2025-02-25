# models.py
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Soporte(BaseModel):
    nombre: str
    grupo_remedy: str
    telefono: str
    correo: str

class Type(str, Enum):
 smc = "smc"
 tmc = "tmc"

class Servicio(BaseModel):
    nombre : Type
    soporte: Soporte
   
class Aplicacion(BaseModel):
    id: Optional[UUID] = uuid4()
    nombre: str
    descripcion: str
    url: str
    marca: str
    dominio: str
    responsable: str
    first_nivel: list[Servicio]
    second_nivel: list[Servicio]
    tercer_nivel: list[Servicio]
    coordinador: list[Servicio]
    horario_servicio: str
    horario_atencion: str
    ventana_intervencion: str
    ventana_intervencion_semanal: str
    ventana_intervencion_mensual: str
    observaciones: str
    centro_afectado: str
    impacto_negocio: str
