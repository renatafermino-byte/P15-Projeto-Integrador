Projeto Integrador P15

Objetivo
Desenvolver um pipeline de dados completo contemplando coleta de dados, armazenamento em PostgreSQL, ETL em Python, engenharia de features e aplicação de Machine Learning para previsão de vendas.

Integrantes
Renata Fermino Ferrari
Tecnologias Utilizadas
Python
PostgreSQL (Neon)
Pandas
Scikit-Learn
Google Colab
GitHub

Estrutura do Projeto
P15-Projeto-Integrador/
│
├── README.md
├── requirements.txt
├── datasets/
├── sql/
├── etl/
├── features/
├── model/
├── notebooks/
└── resultados/

Fontes de Dados
Foram utilizados dois conjuntos de dados:

clientes.csv
vendas.csv
Os dados foram integrados para construção do dataset analítico utilizado no treinamento do modelo.

Pipeline de Dados
clientes.csv
        \
         -> ETL Python -> PostgreSQL
        /
vendas.csv

PostgreSQL
      ↓
Feature Engineering
      ↓
Machine Learning
      ↓
Avaliação
Banco de Dados
Foram criadas duas tabelas:

clientes
vendas
Relacionadas pela chave:

id_cliente
Processo ETL
O processo ETL realiza:

Extração dos arquivos CSV;
Transformação por meio da integração dos dados;
Cálculo do valor total das vendas;
Geração do dataset consolidado.
Engenharia de Features
Foram criadas as seguintes variáveis:

valor_total
mes
ano
faixa_idade
Modelo de Machine Learning
Foi utilizado o algoritmo:

Linear Regression
Biblioteca:

Scikit-Learn
Avaliação
Métrica utilizada:

RMSE (Root Mean Squared Error)
O RMSE mede o erro médio das previsões realizadas pelo modelo.

Como Executar
Instalar dependências:

pip install -r requirements.txt
Executar ETL:

python etl/etl_pipeline.py
Gerar Features:

python features/feature_engineering.py
Treinar Modelo:

python model/train_model.py
Avaliar Modelo:

python model/evaluate_model.py
Resultados
O pipeline foi executado com sucesso, contemplando todas as etapas exigidas pela atividade:

Coleta dos dados;
Armazenamento em PostgreSQL;
ETL em Python;
Engenharia de Features;
Treinamento do modelo;
Avaliação por RMSE.

Conclusão
O projeto permitiu construir um pipeline completo de dados e Machine Learning, demonstrando a integração entre banco de dados PostgreSQL, processamento em Python e modelagem preditiva.