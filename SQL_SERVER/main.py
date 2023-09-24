# python3 -m venv venv
# venv\Scripts\activate
#pip install fastapi
#pip install "uvicorn[standard]"
#pip install redis-om
# uvicorn main:app --reload --port 8000

from turtle import st
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.params import Depends
from starlette.responses import RedirectResponse
import models,schemas
from conexion import SessionLocal,engine
from sqlalchemy.orm import Session

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
  
app = FastAPI()

@app.get('/usuarios/',response_model=List[schemas.User])
def show_users(db:Session=Depends(get_db)):
    usuarios = db.query(models.User).all()
    print(usuarios)
    return usuarios

@app.get("/products")
def all():
    return '[format(x) for x in Product.all_pks()]'

@app.get("/cliente/contado/todos")
def get():
   
    CLIENTES_CONTADO = {
        "CLIENTES": [
        {
            "CODIGO": " 4-123-1026",
            "NOMBRE": "MANUEL QUIROZ",
            "TIPO":"CONTADO"
        },{
            "CODIGO": " 4-123-1029",
            "NOMBRE": "MANUEL QUIROZ",
            "TIPO":"CONTADO"
        }]
    }
    return CLIENTES_CONTADO

@app.get("/cliente/cooporativo/todos")
def get():

    CLIENTES_COOPORATIVO = {
    "CLIENTES_COORPORATIVOS": [
        {
            "CODIGO": "A0084",
            "NOMBRE": "QUINTERO, HUMBERTO",
            "TIPO": "ASOCIADO"
        },
        {
            "CODIGO": "A0420",
            "NOMBRE": "MORALES, EFRAIN/GANADERA MORMAR,S.A",
            "TIPO": "ASOCIADO"
        },
        {
            "CODIGO": "A0485",
            "NOMBRE": "DE LEON ESPINOZA, NILO H.",
            "TIPO": "ASOCIADO"
        },
        {
            "CODIGO": "A0582",
            "NOMBRE": "ARMUELLES C. NECTALIS",
            "TIPO": "ASOCIADO"
        }]
    }
    return CLIENTES_COOPORATIVO


@app.delete("/products/{pk}")
def delete(pk:str):
    return pk

@app.post("/products")
def create(product:str):
    print(product) 
