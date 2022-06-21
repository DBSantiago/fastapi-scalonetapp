from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr
from pydantic import validator


class ResponseModel(BaseModel):
    class Config:
        orm_mode = True


# ================================
#           SELECCION
# ================================
class SeleccionBaseModel(BaseModel):
    pais: str


class SeleccionResponseModel(ResponseModel):
    id: int
    pais: str


# ================================
#           EQUIPO
# ================================
class EquipoBaseModel(BaseModel):
    nombre: str

    @validator("nombre")
    def validate_nombre_length(cls, nombre):
        if len(nombre) <= 1:
            raise ValueError("El nombre del equipo debe tener al menos 2 caracteres.")

        return nombre


class EquipoResponseModel(ResponseModel):
    id: int
    nombre: str


# ================================
#           ROL
# ================================
class RolBaseModel(BaseModel):
    titulo: str


class RolResponseModel(ResponseModel):
    id: int
    titulo: str


# ================================
#           INTEGRANTE
# ================================
class IntegranteBaseModel(BaseModel):
    nombre: str
    apodo: str
    apellido: str
    edad: int
    num_camiseta: int
    seleccion_id: int
    equipo_id: int
    rol_id: int


class IntegranteResponseModel(ResponseModel):
    id: int
    nombre: str
    apodo: str
    apellido: str
    edad: int
    num_camiseta: int
    seleccion: SeleccionResponseModel
    equipo: EquipoResponseModel
    rol: RolResponseModel


class IntegranteXSeleccionModel(IntegranteBaseModel, ResponseModel):
    id: int
    equipo: EquipoResponseModel


class IntegranteXEquipoModel(IntegranteBaseModel, ResponseModel):
    id: int
    seleccion: SeleccionResponseModel


class IntegrantesXSeleccionResponseModel(ResponseModel):
    seleccion: SeleccionResponseModel
    integrantes: List[IntegranteXSeleccionModel]


class IntegrantesXEquipoResponseModel(ResponseModel):
    equipo: EquipoResponseModel
    integrantes: List[IntegranteXEquipoModel]


# ================================
#           USUARIO
# ================================
class UsuarioBaseModel(BaseModel):
    email: EmailStr
    password: str


class UsuarioResponseModel(ResponseModel):
    id: int
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
