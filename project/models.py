from sqlalchemy import Column, Integer, String, ForeignKey, text, Boolean
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship

from .database import Base


# ================================
#           SELECCION
# ================================
class Seleccion(Base):
    __tablename__: str = "selecciones"
    id: int = Column(Integer(), primary_key=True, nullable=False)
    pais: str = Column(String(100), nullable=False)


# ================================
#           EQUIPO
# ================================
class Equipo(Base):
    __tablename__: str = "equipos"
    id: int = Column(Integer(), primary_key=True, nullable=False)
    nombre: str = Column(String(100), nullable=False)


# ================================
#           ROL
# ================================
class Rol(Base):
    __tablename__: str = "roles"
    id: int = Column(Integer(), primary_key=True, nullable=False)
    titulo: str = Column(String(50), nullable=False)


# ================================
#           INTEGRANTE
# ================================
class Integrante(Base):
    __tablename__ = "integrantes"
    id: int = Column(Integer(), primary_key=True, nullable=False)
    nombre: str = Column(String(50), nullable=False)
    apodo: str = Column(String(50))
    apellido: str = Column(String(50), nullable=False)
    edad: int = Column(Integer())
    num_camiseta: int = Column(Integer())
    seleccion_id: int = Column(Integer(), ForeignKey("selecciones.id"), nullable=False)
    equipo_id: int = Column(Integer(), ForeignKey("equipos.id"), nullable=False)
    rol_id: int = Column(Integer(), ForeignKey("roles.id"), nullable=False)
    seleccion = relationship("Seleccion", backref="integrantes")
    equipo = relationship("Equipo", backref="integrantes")
    rol = relationship("Rol", backref="integrantes")


# ================================
#           USUARIO
# ================================
class Usuario(Base):
    __tablename__ = "usuarios"
    id: int = Column(Integer, primary_key=True, nullable=False)
    email: str = Column(String, nullable=False, unique=True)
    password: str = Column(String, nullable=False)
    is_admin: bool = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
