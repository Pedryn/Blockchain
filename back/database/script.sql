create database IF NOT EXISTS Blockchain;

use Blockchain;

CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(8) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    password_hash VARCHAR(64) NOT NULL,
    saldo FLOAT DEFAULT 50
);

CREATE TABLE IF NOT EXISTS cryptos (
    symbol VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50),
    price FLOAT
);

CREATE TABLE IF NOT EXISTS user_cryptos (
    user_id VARCHAR(8),
    symbol VARCHAR(10),
    amount FLOAT,
    PRIMARY KEY (user_id, symbol),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (symbol) REFERENCES cryptos(symbol)
);

CREATE TABLE IF NOT EXISTS blocks (
    block_index INT PRIMARY KEY,
    previous_hash VARCHAR(64),
    hash VARCHAR(64),
    transactions TEXT,
    nonce INT,
    timestamp DOUBLE
);


select * from users;

SELECT u.id, 
       u.name, 
       ROUND(SUM(uc.amount * c.price) + u.saldo, 2) AS saldo_total
FROM users u
INNER JOIN user_cryptos uc ON u.id = uc.user_id
INNER JOIN cryptos c ON uc.symbol = c.symbol
GROUP BY u.id, u.name;

select * from blocks;

drop database Blockchain;
