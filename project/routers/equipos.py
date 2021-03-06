from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from project import crud
from project.database import get_db
from project.models import Usuario
from project.oauth2 import get_current_usuario
from project.schemas import EquipoResponseModel, EquipoBaseModel, TokenData

router = APIRouter(prefix="/equipos")


@router.get("/", response_model=List[EquipoResponseModel], tags=["equipos"])
async def get_equipos(db: Session = Depends(get_db)):
    equipos = crud.get_equipos(db)

    return [equipo for equipo in equipos]


@router.get("/{equipo_id}", response_model=EquipoResponseModel, tags=["equipos"])
async def get_equipo(equipo_id: int, db: Session = Depends(get_db)):
    equipo = crud.get_equipo(db, equipo_id)

    if equipo is None:
        raise HTTPException(status_code=404, detail="Equipo no encontrado.")

    return equipo


@router.post("/", response_model=EquipoResponseModel, tags=["equipos"])
async def create_equipo(equipo: EquipoBaseModel, db: Session = Depends(get_db),
                        current_usuario: Usuario = Depends(get_current_usuario)):
    if current_usuario.is_admin is False:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Solo usuarios administradores pueden crear equipos.")

    new_equipo = crud.create_equipo(db, equipo)

    if new_equipo is None:
        raise HTTPException(status_code=404, detail="Equipo no encontrado.")

    return new_equipo


@router.put("/{equipo_id}", response_model=EquipoResponseModel, tags=["equipos"])
async def update_equipo(equipo: EquipoBaseModel, equipo_id: int, db: Session = Depends(get_db),
                        current_usuario: Usuario = Depends(get_current_usuario)):
    if current_usuario.is_admin is False:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Solo usuarios administradores pueden modificar equipos.")

    new_equipo = crud.update_equipo(db, equipo, equipo_id)

    if new_equipo is None:
        raise HTTPException(status_code=404, detail="Equipo no encontrado.")

    return new_equipo


@router.delete("/{equipo_id}", response_model=EquipoResponseModel, tags=["equipos"])
async def delete_equipo(equipo_id: int, db: Session = Depends(get_db),
                        current_usuario: Usuario = Depends(get_current_usuario)):
    if current_usuario.is_admin is False:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Solo usuarios administradores pueden eliminar equipos.")

    deleted_equipo = crud.delete_equipo(db, equipo_id)

    if deleted_equipo is None:
        raise HTTPException(status_code=404, detail="Equipo no encontrado.")

    return deleted_equipo
