# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Pratique manipulação de strings, loops, condicionais e seleção aleatória construindo o clássico jogo da forca, onde o jogador tenta adivinhar uma palavra oculta letra por letra.

## 📝 Tarefas

### 🛠️	Seleção da Palavra e Estado Inicial

#### Descrição
Selecione aleatoriamente uma palavra secreta de uma lista predefinida e inicialize as variáveis que controlam o estado do jogo.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra de uma lista predefinida (`words`)
- Inicializar o conjunto/lista de letras já adivinhadas (vazio no início)
- Inicializar o contador de tentativas incorretas (0 no início)
- Definir o número máximo de tentativas incorretas permitidas


### 🛠️	Loop Principal e Resultado do Jogo

#### Descrição
Implemente o loop principal que exibe o progresso, recebe os palpites do jogador e determina o fim de jogo (vitória ou derrota).

#### Requisitos
O programa concluído deve:

- Exibir o progresso atual da palavra no formato `_ _ _`
- Aceitar palpites de letras via `input()` do usuário
- Atualizar letras adivinhadas e tentativas incorretas restantes
- Encerrar o loop quando a palavra for totalmente adivinhada ou as tentativas se esgotarem
- Exibir uma mensagem de vitória ou de derrota ao final