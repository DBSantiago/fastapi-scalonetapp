from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from project.database import get_db
from project import crud
from project.schemas import RolResponseModel, RolBaseModel

router = APIRouter(prefix="/roles")


@router.get("/", response_model=List[RolResponseModel], tags=["roles"])
async def get_roles(db: Session = Depends(get_db)):
    roles = crud.get_roles(db)

    return [rol for rol in roles]


@router.get("/{rol_id}", response_model=RolResponseModel, tags=["roles"])
async def get_rol(rol_id: int, db: Session = Depends(get_db)):
    rol = crud.get_rol(db, rol_id)

    if rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado.")

    return rol


@router.post("/", response_model=RolResponseModel, tags=["roles"])
async def create_rol(rol: RolBaseModel, db: Session = Depends(get_db)):
    new_rol = crud.create_rol(db, rol)

    return new_rol


@router.put("/{rol_id}", response_model=RolResponseModel, tags=["roles"])
async def update_rol(rol: RolBaseModel, rol_id: int, db: Session = Depends(get_db)):
    new_rol = crud.update_rol(db, rol, rol_id)

    if new_rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado.")

    return new_rol


@router.delete("/{rol_id}", response_model=RolResponseModel, tags=["roles"])
async def delete_rol(rol_id: int, db: Session = Depends(get_db)):
    deleted_rol = crud.delete_rol(db, rol_id)

    if deleted_rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado.")

    return deleted_rol
