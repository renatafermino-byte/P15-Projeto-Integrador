COPY clientes
FROM 'clientes.csv'
DELIMITER ','
CSV HEADER;

COPY vendas
FROM 'vendas.csv'
DELIMITER ','
CSV HEADER;