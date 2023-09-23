from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    CLIENTE:str
    NOMBRE:str

    class Config:
        orm_mode =True

class UserUpdate(BaseModel):   
    nombre:str
   

    class Config:
        orm_mode =True

class Respuesta(BaseModel):   
    mensaje:str
   