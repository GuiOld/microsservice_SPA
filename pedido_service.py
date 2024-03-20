from fastapi import FastAPI
import json

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

app = FastAPI()

pedido_data = "pedido.txt"
login_data = leitura("login.txt")

@app.post("/pedido/{user_id}/add")
async def criar_pedido(user_id: int):
   if int(user_id) != int(login_data.get("user_id")):
      return {"status": "Erro", "mensagem": "Usuário não encontrado"}
   
   data = {"id": user_id, "order_id": 123}
   escrita(pedido_data, data)
   return {"status": "sucesso", "mensagem": "Pedido criado", "order_id": 123}

@app.get("/pedido")
async def getPedidoInfo():
    data = leitura(pedido_data)
    return data