from fastapi import FastAPI
import random
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel):
    nome: str
    curso: str
    ativo: bool 

@app.get("/")
async def root():
    return {"message": "Hello World"}


# http://127.0.0.1:8000/teste1

@app.get("/funcaoteste")
async def funcaoteste():
    return{"Teste": True, "num_aleatório" : random.randint(0, 50000)}

@app.post("/estudante/cadastro")
async def cadastrar_estudante(estudante: Estudante):
    return estudante

@app.put("/estudante/update/{id_estudante}")
async def atualizar_estudante(id_estudante: int):
    return id_estudante > 0

@app.delete("/estudante/delete/{id_estudante}")
async def deletar_estudante(id_estudante: int):
    return id_estudante > 0