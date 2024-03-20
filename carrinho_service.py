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

cart = {}

carrinho_data = "carrinho.txt"
login_data = leitura("login.txt")
produto_data = leitura("produtos.txt")

@app.post("/carrinho/{user_id}/{produto_id}/{quantidade}/add")
async def add_carrinho(user_id: int, produto_id: int, quantidade: int):
    if int(user_id) != int(login_data.get("user_id")):
        return {"status": "Erro", "mensagem": "Usuário não encontrado"}
    
    for produto in produto_data.get("produtos", []):
        if produto["id"] == produto_id:
            produto_encontrado = produto
            break

    if user_id not in cart:
        cart[user_id] = []
    carrinho_usuario = {"produto_id": produto_id, "quantidade": quantidade}
    cart[user_id].append(carrinho_usuario)
    escrita(carrinho_data, cart)
    
    return {"status": "Sucesso", "mensagem": "Produto adicionado ao carrinho"}

@app.get("/carrinho")
async def getCarrinhoinfo():
    data = leitura(carrinho_data)
    return data 


