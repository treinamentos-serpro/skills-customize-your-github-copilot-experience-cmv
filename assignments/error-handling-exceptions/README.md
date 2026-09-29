# 📘 Tarefa: Error Handling & Custom Exceptions

## 🎯 Objective

Aprenda a lidar com erros de forma robusta em Python usando `try/except/else/finally` e a criar exceções customizadas para validação defensiva.

## 📝 Tasks

### 🛠️ Tratar Erros Comuns com Try/Except

#### Descrição
Escreva uma função `safe_divide(a, b)` que trate erros de divisão e de tipo usando `try/except/else/finally`.

#### Requisitos
O programa completo deve:

- Usar `try/except` para capturar `ZeroDivisionError` e `TypeError`
- Retornar o resultado da divisão no bloco `else` quando não houver erro
- Usar `finally` para imprimir uma mensagem indicando que a operação terminou
- Retornar `None` e imprimir uma mensagem de erro apropriada quando uma exceção ocorrer

### 🛠️ Criar uma Exceção Customizada

#### Descrição
Defina uma exceção customizada `InsufficientFundsError` e utilize-a para validar saques em uma função `withdraw(balance, amount)`.

#### Requisitos
O programa completo deve:

- Criar uma classe `InsufficientFundsError` que herde de `Exception`
- Levantar (`raise`) `InsufficientFundsError` quando `amount` for maior que `balance`
- Retornar o novo saldo quando o saque for válido
- Demonstrar a captura da exceção com um bloco `try/except`

### 🛠️ Validação Defensiva com Múltiplas Exceções

#### Descrição
Escreva uma função `process_order(item, quantity, price)` que valide as entradas e levante exceções apropriadas para diferentes casos de erro.

#### Requisitos
O programa completo deve:

- Levantar `ValueError` quando `quantity` ou `price` forem negativos
- Levantar uma exceção customizada `OutOfStockError` quando `quantity` for zero
- Capturar as exceções em um bloco `try/except` com múltiplos blocos `except`
- Retornar o custo total (`quantity * price`) quando a validação for bem-sucedida
