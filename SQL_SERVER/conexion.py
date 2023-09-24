from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.engine import URL

SERVER = '192.168.10.11'
DATABASE = 'SOFTLAND'
USERNAME = 'sa'
PASSWORD = '4dm1n@C00l3ch3'

connection_url = URL.create(
    "mssql+pymssql",
    username=USERNAME,
    password=PASSWORD,
    host=SERVER,
    database=DATABASE
)

engine = create_engine(connection_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
