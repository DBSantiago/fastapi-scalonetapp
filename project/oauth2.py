from datetime import datetime, timedelta

from decouple import config
from jose import JWTError, jwt
from fastapi import status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from project.database import get_db
from project.models import Usuario
from project.schemas import TokenData

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 8

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict):
    data_copy = data.copy()
    expiration_time = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)

    data_copy.update({"exp": expiration_time})

    encoded_jwt = jwt.encode(data_copy, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception: Exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        usuario_id: str = payload.get("usuario_id")

        if id is None:
            raise credentials_exception

        token_data = TokenData(id=usuario_id)
    except JWTError:
        raise credentials_exception

    return token_data


def get_current_usuario(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="No pudimos validar las credenciales",
                                          headers={"WWW-Authenticate": "Bearer"})

    token_data = verify_access_token(token, credentials_exception)

    current_usuario = db.query(Usuario).filter(Usuario.id == token_data.id).first()

    return current_usuario
