CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    cidade VARCHAR(100),
    idade INT,
    sexo VARCHAR(10)
);

CREATE TABLE vendas (
    id_venda INT PRIMARY KEY,
    id_cliente INT,
    data_venda DATE,
    produto VARCHAR(100),
    quantidade INT,
    preco_unitario NUMERIC(10,2),
    FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente)
);