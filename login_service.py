from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

#função de leitura
def leitura(arquivo):
    try:
        with open(arquivo, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def escrita(arquivo, data):
    with open(arquivo, "w") as file:
        json.dump(data, file)

login_data = "login.txt"

@app.post("/login/{username}/{password}")
async def login(username: str, password: str):
    if username == "user" and password == "password":
        data = {"id": 0, "username": username, "password": password}
        escrita(login_data, data)
        return {"status": "sucesso", "mensagem": "Usuário autenticado"}
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

@app.get("/login")
async def getLogininfo():
    data = leitura(login_data)
    return data