import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY ,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    curso TEXT NOT NULL,
    genero TEXT NOT NULL
)
""")

# Inserir 23 usuários de exemplo
for i in range(1, 4):
    cursor.execute("""
    INSERT INTO usuarios (id, nome, idade, curso, genero)
    VALUES (?, ?, ?, ?, ?)
    """, (
        i,
        f"Usuário {i}",
        18 + (i % 5),
        f"Curso {i % 4}",
        ["Masculino", "Feminino", "Outro"][i % 3]
    ))

conn.commit()
conn.close()
