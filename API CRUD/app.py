from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def conectar():
    return sqlite3.connect("banco.db")

@app.route("/usuarios", methods=["GET"])
def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    dados = cursor.fetchall()
    conn.close()

    usuarios = [{"id": u[0], "nome": u[1], "idade": u[2], "curso": u[3], "genero": u[4]} for u in dados]
    return jsonify(usuarios)

@app.route("/usuarios", methods=["POST"])
def criar():
    dados = request.get_json()
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuarios (id, nome, idade, curso, genero)
        VALUES (?, ?, ?, ?, ?)
    """, (dados["id"], dados["nome"], dados["idade"], dados["curso"], dados["genero"]))
    conn.commit()
    conn.close()
    return jsonify(dados), 201

@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE usuarios
        SET nome = ?, idade = ?, curso = ?, genero = ?
        WHERE id = ?
    """, (dados["nome"], dados["idade"], dados["curso"], dados["genero"], id))
    conn.commit()
    conn.close()
    return jsonify(dados)

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Usuário deletado"}), 200

if __name__ == "__main__":
    app.run(debug=True)
