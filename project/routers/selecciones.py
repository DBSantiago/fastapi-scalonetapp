from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from project import crud
from project.database import get_db
from project.models import Usuario
from project.oauth2 import get_current_usuario
from project.schemas import SeleccionResponseModel, SeleccionBaseModel, TokenData

router = APIRouter(prefix="/selecciones")


@router.get("/", response_model=List[SeleccionResponseModel], tags=["selecciones"])
async def get_selecciones(db: Session = Depends(get_db)):
    selecciones = crud.get_selecciones(db)

    return [seleccion for seleccion in selecciones]


@router.get("/{seleccion_id}", response_model=SeleccionResponseModel, tags=["selecciones"])
async def get_seleccion(seleccion_id: int, db: Session = Depends(get_db)):
    seleccion = crud.get_seleccion(db, seleccion_id)

    if seleccion is None:
        raise HTTPException(status_code=404, detail="Selección no encontrada")

    return seleccion


@router.post("/", response_model=SeleccionResponseModel, tags=["selecciones"])
async def create_seleccion(seleccion: SeleccionBaseModel, db: Session = Depends(get_db),
                           current_usuario: Usuario = Depends(get_current_usuario)):
    if current_usuario.is_admin is False:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Solo usuarios administradores pueden agregar selecciones.")

    new_seleccion = crud.create_seleccion(db, seleccion)

    return new_seleccion


@router.put("/{seleccion_id}", response_model=SeleccionResponseModel, tags=["selecciones"])
async def update_seleccion(seleccion: SeleccionBaseModel, seleccion_id: int, db: Session = Depends(get_db),
                           current_usuario: Usuario = Depends(get_current_usuario)):
    if current_usuario.is_admin is False:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Solo usuarios administradores pueden modificar selecciones.")

    updated_seleccion = crud.update_seleccion(db, seleccion, seleccion_id)

    if updated_seleccion is None:
        raise HTTPException(status_code=404, detail="Selección no encontrada")

    return updated_seleccion


@router.delete("/{seleccion_id}", response_model=SeleccionResponseModel, tags=["selecciones"])
async def delete_seleccion(seleccion_id: int, db: Session = Depends(get_db),
                           current_usuario: Usuario = Depends(get_current_usuario)):
    if current_usuario.is_admin is False:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Solo usuarios administradores pueden eliminar selecciones.")

    deleted_seleccion = crud.delete_seleccion(db, seleccion_id)

    if deleted_seleccion is None:
        raise HTTPException(status_code=404, detail="Selección no encontrada")

    return deleted_seleccion
