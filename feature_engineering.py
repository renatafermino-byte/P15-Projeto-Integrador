import pandas as pd

dados = pd.read_csv("../datasets/dataset_final.csv")

dados["data_venda"] = pd.to_datetime(
    dados["data_venda"]
)

dados["mes"] = dados["data_venda"].dt.month

dados["ano"] = dados["data_venda"].dt.year

dados["faixa_idade"] = pd.cut(
    dados["idade"],
    bins=[0, 25, 40, 60, 100],
    labels=[1, 2, 3, 4]
)

dados.to_csv(
    "../datasets/dataset_features.csv",
    index=False
)

print("Features criadas com sucesso!")