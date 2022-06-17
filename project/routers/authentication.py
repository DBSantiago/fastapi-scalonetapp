from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from project.database import get_db
from project import crud, utils, oauth2
from project.schemas import UsuarioBaseModel

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/login")
def login(usuario_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = crud.get_usuario_by_email(db, usuario_credentials)

    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials.")

    if not utils.verify_password(usuario_credentials.password, usuario.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials.")

    usuario_data = {
        "usuario_id": usuario.id
    }
    access_token = oauth2.create_access_token(data=usuario_data)

    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }
