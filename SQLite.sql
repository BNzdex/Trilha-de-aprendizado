CREATE TABLE Cliente (
Id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
nome_cliente VARCHAR(100) not NULL,
cpf CHAR(11) NOT NULL,
endereço VARCHAR(100) NOT NULL
);
  
  
CREATE TABLE Produtos (
Id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
nome_produto VARCHAR(100) NOT NULL,
quantidade_estoque INT NOT NULL,
valor VARCHAR(11)
 );

INSERT INTO Cliente (nome_cliente,cpf,endereço)  VALUES
('Bernardo Locatelli', '17397323758', 'Rua Uruguai, 179'),
('Lorrany', '98976598123', 'Rua Alfonso Claudio, 99'),
('Maria', '62351749629', 'Rua XI, 157'), 
('Ivo', '84325128552', 'Rua Edilson Santos, 876'),
('Lolo', '45183139784', 'Rua X, 77');

INSERT INTO Produtos(nome_produto, quantidade_estoque, valor) VALUES
('Mouse', 55, 'R$30,00'),
('Teclado', 64, 'R$50,00'),
('Placa de vídeo', 13, 'R$2000,00'),
('Fone', 20, 'R$200,00'),
('Cadeira gamer', 5, 'R$800,00');
