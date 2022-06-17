from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from project import crud
from project.database import get_db
from project.oauth2 import get_current_usuario
from project.schemas import IntegranteResponseModel, IntegranteBaseModel

router = APIRouter(prefix="/integrantes")


@router.get("/", response_model=List[IntegranteResponseModel], tags=["integrantes"])
async def get_integrantes(db: Session = Depends(get_db)):
    integrantes = crud.get_integrantes(db)

    return [integrante for integrante in integrantes]


@router.get("/{integrante_id}", response_model=IntegranteResponseModel, tags=["integrantes"])
async def get_integrante(integrante_id: int, db: Session = Depends(get_db)):
    integrante = crud.get_integrante(db, integrante_id)

    if integrante is None:
        raise HTTPException(status_code=404, detail="Integrante no encontrado")

    return integrante


@router.post("/", response_model=IntegranteResponseModel, tags=["integrantes"])
async def create_integrante(integrante: IntegranteBaseModel, db: Session = Depends(get_db),
                            usuario_id: int = Depends(get_current_usuario)):
    new_integrante = crud.create_integrante(db, integrante)

    return new_integrante


@router.put("/{integrante_id}", response_model=IntegranteResponseModel, tags=["integrantes"])
async def update_integrante(integrante: IntegranteBaseModel, integrante_id: int, db: Session = Depends(get_db),
                            usuario_id: int = Depends(get_current_usuario)):
    updated_integrante = crud.update_integrante(db, integrante, integrante_id)

    if updated_integrante is None:
        raise HTTPException(status_code=404, detail="Integrante no encontrado")

    return updated_integrante


@router.delete("/{integrante_id}", tags=["integrantes"])
async def delete_integrante(integrante_id: int, db: Session = Depends(get_db),
                            usuario_id: int = Depends(get_current_usuario)):
    deleted_integrante = crud.delete_integrante(db, integrante_id)

    if deleted_integrante is None:
        raise HTTPException(status_code=404, detail="Integrante no encontrado")

    return deleted_integrante
