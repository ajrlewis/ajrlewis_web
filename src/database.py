import os

from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL", "mysql+pymysql://")
if not SQLALCHEMY_DATABASE_URL:
    message = f"SQLALCHEMY_DATABASE_URL not set, unable to make SessionLocal object."
    logger.error(message)
    # raise ValueError(message)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
