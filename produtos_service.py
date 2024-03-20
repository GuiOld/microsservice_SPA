from fastapi import FastAPI
import json

app = FastAPI()

def leitura(arquivo):
    try:
        with open(arquivo, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def escrita(arquivo, data):
    with open(arquivo, "w") as file:
        json.dump(data, file)

produto_data = "produtos.txt"

@app.post("/produtos/{nome}/{preco}")
async def add_produtos(nome: str, preco: int):
    data = leitura(produto_data)
    produtos = data["produtos"]
    novo_produto = {"id": len(produtos) + 1, "nome": nome, "preco": preco}
    produtos.append(novo_produto)
    data["produtos"] = produtos
    escrita(produto_data, data)
    return {"status": "sucesso", "mensagem": "Produto adicionado com sucesso", "produto": novo_produto}

@app.get("/produtos")
async def listar_produtos():
    data = leitura(produto_data)
    return data
