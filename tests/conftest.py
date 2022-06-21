from datetime import datetime

import pytest
from decouple import config
from jose import jwt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient

from project import app
from project.database import get_db, Base
from project.models import Usuario, Equipo
from project.oauth2 import SECRET_KEY, ALGORITHM
from project.schemas import Token
from project.utils import hash_password

TEST_DB_HOST = config("TEST_DB_HOST")
TEST_DB_USER = config("TEST_DB_USER")
TEST_DB_PASSWORD = config("TEST_DB_PASSWORD")
TEST_DB_PORT = config("TEST_DB_PORT")
# SQLALCHEMY_DATABASE_URL = config("DATABASE_URL_2")

ADMIN_EMAIL = config("ADMIN_EMAIL")
ADMIN_PASSWORD = hash_password(config("ADMIN_PASSWORD"))

SQLALCHEMY_TEST_DATABASE_URL = f"postgresql://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_HOST}:{TEST_DB_PORT}/test_scalonetapp"

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        """
        Creates a SQLAlchemy SessionLocal dependency that will be used in a single request.
        It is closed once the request is finished.
        """
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def usuario_test(session):
    new_usuario = Usuario(email="test@email.com", password=hash_password("password123"))

    session.add(new_usuario)
    session.commit()
    session.refresh(new_usuario)

    return {
        "id": new_usuario.id,
        "email": new_usuario.email,
        "password": "password123"
    }


@pytest.fixture
def usuario_login(client, usuario_test):
    response = client.post("/api/v1/auth/login", data={"username": usuario_test.get("email"),
                                                       "password": usuario_test.get("password")})

    login_res = Token(**response.json())
    payload = jwt.decode(login_res.access_token, SECRET_KEY, algorithms=[ALGORITHM])
    usuario_id = payload.get("usuario_id")

    assert usuario_id == usuario_test.get("id")

    return login_res


@pytest.fixture
def admin_test(session):
    new_admin = Usuario(email=ADMIN_EMAIL, password=hash_password(ADMIN_PASSWORD), is_admin=True,
                        created_at=datetime.utcnow())

    session.add(new_admin)
    session.commit()
    session.refresh(new_admin)

    return {
        "id": new_admin.id,
        "email": new_admin.email,
        "password": ADMIN_PASSWORD,
        "is_admin": new_admin.is_admin,
    }


@pytest.fixture
def admin_login(client, admin_test):
    response = client.post("/api/v1/auth/login",
                           data={"username": admin_test.get("email"),
                                 "password": admin_test.get("password")})

    login_res = Token(**response.json())
    payload = jwt.decode(login_res.access_token, SECRET_KEY, algorithms=[ALGORITHM])
    usuario_id = payload.get("usuario_id")

    assert usuario_id == admin_test.get("id")

    return login_res


@pytest.fixture
def equipo_test(client, session):
    new_equipo = Equipo(nombre="equipo_test")

    session.add(new_equipo)
    session.commit()
    session.refresh(new_equipo)

    return {
        "id": new_equipo.id,
        "nombre": new_equipo.nombre
    }
