CREATE TABLE Cliente (
Id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
nome_cliente VARCHAR(100) not NULL,
cpf CHAR(11) NOT NULL,
endereço VARCHAR(100) NOT NULL,
telefone CHAR(11)
);
  
  
CREATE TABLE Produtos (
Id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
nome_produto VARCHAR(100) NOT NULL,
quantidade_estoque INT NOT NULL,
valor INT
 );

INSERT INTO Cliente (nome_cliente,cpf,endereço)  VALUES
('Bernardo Locatelli', '17397323758', 'Rua Uruguai, 179', '27996283448'),
('Lorrany', '98976598123', 'Rua Alfonso Claudio, 99', '27996783888'),
('Maria', '62351749629', 'Rua XI, 157', '27991287148'), 
('Ivo', '84325128552', 'Rua Edilson Santos, 876', '27996265278'),
('Lolo', '45183139784', 'Rua X, 77', '27994723448');

INSERT INTO Produtos(nome_produto, quantidade_estoque, valor) VALUES
('Mouse', 55, '30'),
('Teclado', 64, '50'),
('Placa de vídeo', 13, '2000'),
('Fone', 20, '200'),
('Cadeira gamer', 5, '800');
