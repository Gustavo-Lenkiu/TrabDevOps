from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


# http://127.0.0.1:8000/teste1
@app.get("/funcaoteste")
async def funcaoteste():
    return{"Teste": "Deu certo"}