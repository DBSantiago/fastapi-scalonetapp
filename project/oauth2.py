from datetime import datetime, timedelta

from decouple import config
from jose import JWTError, jwt

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 8


def create_access_token(data: dict):
    data_copy = data.copy()
    expiration_time = datetime.now() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)

    data_copy.update({"exp": expiration_time})

    encoded_jwt = jwt.encode(data_copy, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
