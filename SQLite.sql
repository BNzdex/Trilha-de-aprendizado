CREATE TABLE Cliente (
Id_cliente INT PRIMARY KEY,
nome_cliente VARCHAR(100) not NULL,
cpf CHAR(11) NOT NULL,
endereço VARCHAR(100) NOT NULL
);
  
  
CREATE TABLE Produtos (
Id_produto INT PRIMARY KEY,
nome_produto VARCHAR(100) NOT NULL,
quantidade_estoque INT NOT NULL
 );