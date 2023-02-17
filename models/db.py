import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


PG_USER = os.environ.get('POSTGRES_USER', 'vitya')
PG_PASSWORD = os.environ.get('POSTGRES_PASSWORD', '1')
PG_DB = os.environ.get('POSTGRES_DB', 'clients')
PG_HOST = os.environ.get('POSTGRES_HOST', 'localhost')

SQLALCHEMY_DATABASE_URL = \
    f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{PG_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()