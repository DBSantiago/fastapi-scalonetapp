from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

DB_HOST = config("DB_HOST")
DB_USER = config("DB_USER")
DB_PASSWORD = config("DB_PASSWORD")
DB_PORT = config("DB_PORT")
# SQLALCHEMY_DATABASE_URL = config("DATABASE_URL_2")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/db_scalonetapp"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Creates a SQLAlchemy SessionLocal dependency that will be used in a single request.
    It is closed once the request is finished.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
