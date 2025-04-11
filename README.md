# 🪙 Catálogo de criptomoedas com Blockchain

Este projeto foi desenvolvido como parte da disciplina Segurança de Aplicações, com o objetivo de simular um sistema catálogo de critomoedas utilizando os princípios da tecnologia Blockchain para garantir transações seguras no sistema.

## 📌 Sobre o Projeto

- A aplicação permite que usuários possam comprar, vender e transferir criptomoedas fictícias entre os usuários. Cada transação realizada é registrada em um bloco, que é minado (Proof of Work) e adicionado à blockchain.
- Scripts garantem que as criptomoedas valorizem ou desvalorizem aleatóriamente e realizam interações aleatórias entre os usuários, para simular volatividade das moedas e interações no sistema.
- A integridade da cadeia é periodicamente verificada, garantindo que nenhuma alteração indevida ocorra nos dados armazenados.

## 🧰 Tecnologias Utilizadas

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white&color=00A0B9"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white&color=00A0B9"/>
  <img src="https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white&color=00A0B9"/>
  <img src="https://img.shields.io/badge/APScheduler-FF5733?style=for-the-badge&logo=clockify&logoColor=white&color=00A0B9"/>
</p>

## 🔄 Funcionalidades
- Registro de transações em blocos

- Mineração com prova de trabalho

- Validação periódica da integridade da cadeia

- Simulação de variação no valor das criptomoedas

## 🔐 Segurança com Blockchain
- A blockchain é utilizada aqui para garantir que cada transação registrada seja imutável e auditável, impedindo alterações posteriores e promovendo confiança nas operações realizadas, mesmo sem um banco centralizado.

## 🚀 Como rodar o projeto

### 1. Clone o repositório

    git clone https://github.com/Pedryn/blockchain.git
    cd blockchain
    cd back

### 2. Crie e inicie um ambiente virtual (Windows)

    python -m venv venv
    venv\Scripts\activate

### 2.1 Crie e inicie um ambiente virtual (Linux / MacOS)

    python3 -m venv venv
    source venv/bin/activate

### 3. Instale as dependências

    pip install -r requirements.txt

### 4. Configure a conexão com o Banco de dados MySQL
Edite o arquivo back/database/config.py e substitua com os dados do seu MySQL:

    def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='seu_usuario',
        password='sua_senha',
        database='nome_do_banco'
    )

### 5. Crie o banco de dados em seu MySQL e execute o script
Crie o banco com o comando abaixo e execute o script disponível em back/database/script.sql

    CREATE DATABASE blockchain;

### 6. Rode a aplicação

    flask run