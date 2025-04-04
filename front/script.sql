CREATE DATABASE blockchain;

USE blockchain;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    reais int(50),
    fatecoins int(50) 
);

INSERT INTO users (nome, senha, reais, fatecoins) VALUES
('Pedro', '1234', 50, 10),
('Felipe', 'abcd', 50, 10);
select * from users;


