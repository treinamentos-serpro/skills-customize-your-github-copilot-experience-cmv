# Código Inicial para a Tarefa de REST APIs com FastAPI

from fastapi import FastAPI

app = FastAPI()

# Armazenamento em memória para os itens
items = []

# TODO: Criar um endpoint GET "/items" que retorne a lista de itens

# TODO: Definir um modelo Pydantic "Item" com os campos: name (str) e price (float)

# TODO: Criar um endpoint POST "/items" que receba um Item e adicione à lista

# TODO: Criar um endpoint GET "/items/{item_id}" que retorne o item pelo índice
#       ou um erro 404 se não existir

# TODO: Criar um endpoint DELETE "/items/{item_id}" que remova o item pelo índice
