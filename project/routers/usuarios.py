from typing import List

from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from project.database import get_db
from project import crud
from project.schemas import UsuarioResponseModel, UsuarioBaseModel

router = APIRouter(prefix="/usuarios", tags=["usuarios"])


@router.get("/", response_model=List[UsuarioResponseModel])
async def get_usuarios(db: Session = Depends(get_db)):
    usuarios = crud.get_usuarios(db)

    return [usuario for usuario in usuarios]


@router.get("/{usuario_id}", response_model=UsuarioResponseModel)
async def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud.get_usuario(db, usuario_id)

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario inexistente.")

    return usuario


@router.post("/", response_model=UsuarioResponseModel)
async def create_usuario(usuario: UsuarioBaseModel, db: Session = Depends(get_db)):
    new_usuario = crud.create_usuario(db, usuario)

    return new_usuario


@router.put("/{usuario_id}", response_model=UsuarioResponseModel)
async def update_usuario(usuario_id: int, usuario: UsuarioBaseModel, db: Session = Depends(get_db)):
    updated_usuario = crud.update_usuario(db, usuario, usuario_id)

    if updated_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario inexistente.")

    return updated_usuario


@router.delete("/{usuario_id}")
async def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    deleted_usuario = crud.delete_usuario(db, usuario_id)

    if deleted_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario inexistente.")

    return deleted_usuario
