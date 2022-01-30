from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

database_url= f'mysql+pymysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'
engine =create_engine(database_url)

first_session = sessionmaker(autocommit= False, autoflush=False, bind=engine)

Base = declarative_base()

def get_database():
    db = first_session()
    try:
        yield db
    finally:
        db.close()