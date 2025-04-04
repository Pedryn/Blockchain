const express = require("express");
const mysql = require("mysql");
const cors = require("cors");
const bodyParser = require("body-parser");

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Conexão com o MySQL
const db = mysql.createConnection({
    host: "localhost",
    user: "nodeuser",
    password: "root", // Coloque a senha do MySQL aqui
    database: "blockchain"
});

db.connect(err => {
    if (err) {
        console.error("Erro ao conectar ao MySQL:", err);
        return;
    }
    console.log("Conectado ao MySQL!");
});

// Rota de login
app.post("/login", (req, res) => {
    const { nome, senha } = req.body;
    
    const sql = "SELECT * FROM users WHERE nome = ? AND senha = ?";
    db.query(sql, [nome, senha], (err, result) => {
        if (err) {
            return res.status(500).json({ error: "Erro no servidor" });
        }
        if (result.length > 0) {
            res.json({ success: true, user: result[0] });
        } else {
            res.status(401).json({ success: false, message: "Usuário ou senha inválidos" });
        }
    });
});

// Iniciar o servidor
app.listen(3000, () => {
    console.log("Servidor rodando na porta 3000");
});
