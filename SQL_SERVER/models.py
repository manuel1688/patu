from sqlalchemy import MetaData, Table, String, Column, Text, DateTime, Boolean
from sqlalchemy.orm import mapper
from conexion import Base

metadata = MetaData(schema="COOLECHE")

post = Table('CLIENTE', metadata, 
    Column('CLIENTE', String(200), primary_key=True),
    Column('NOMBRE', String(200),  nullable=False)
)

class User(object):
    pass

mapper(User, post)

# class User(Base):
#     __tablename__ = "CLIENTE"

#     CLIENTE = Column(String, primary_key=True, index=True)
#     NOMBRE = Column(String, unique=True, index=True)



     