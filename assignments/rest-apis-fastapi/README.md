# 📘 Tarefa: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a construir uma API REST em Python usando o framework FastAPI, incluindo validação de dados com Pydantic e tratamento de erros HTTP.

## 📝 Tasks

### 🛠️ Configurar a Aplicação e Endpoint de Listagem

#### Descrição
Configure uma aplicação FastAPI e crie um endpoint que retorna a lista de itens armazenados em memória.

#### Requisitos
O programa completo deve:

- Criar uma instância de `FastAPI`
- Definir uma lista em memória para armazenar os itens
- Implementar o endpoint `GET /items` que retorna a lista completa de itens
- Rodar a aplicação localmente com `uvicorn` e verificar a resposta em `/items`

### 🛠️ Criar Itens com Validação via Pydantic

#### Descrição
Defina um modelo Pydantic para validar os dados recebidos e implemente o endpoint para adicionar novos itens.

#### Requisitos
O programa completo deve:

- Definir um modelo Pydantic `Item` com os campos `name` (str) e `price` (float)
- Implementar o endpoint `POST /items` que receba um `Item` no corpo da requisição
- Adicionar o novo item à lista em memória
- Retornar o item criado na resposta

### 🛠️ Buscar e Remover Itens por ID

#### Descrição
Implemente endpoints para buscar um item específico pelo índice e removê-lo, tratando o caso de item inexistente.

#### Requisitos
O programa completo deve:

- Implementar o endpoint `GET /items/{item_id}` que retorna o item correspondente
- Retornar um erro HTTP 404 quando o `item_id` não existir
- Implementar o endpoint `DELETE /items/{item_id}` que remove o item da lista
- Retornar uma mensagem de confirmação após a remoção
