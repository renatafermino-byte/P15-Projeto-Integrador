import pandas as pd

# Leitura dos arquivos de origem
clientes = pd.read_csv("../datasets/clientes.csv")
vendas = pd.read_csv("../datasets/vendas.csv")

# Integração dos dados
dados = vendas.merge(
    clientes,
    on="id_cliente",
    how="left"
)

# Criação da variável valor_total
dados["valor_total"] = (
    dados["quantidade"] *
    dados["preco_unitario"]
)

# Salvar dataset consolidado
dados.to_csv(
    "../datasets/dataset_final.csv",
    index=False
)

print("ETL executado com sucesso!")