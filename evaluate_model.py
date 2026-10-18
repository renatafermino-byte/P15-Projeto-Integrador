import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Carregar dataset
dados = pd.read_csv("../datasets/dataset_features.csv")

# Features
X = dados[
    [
        "quantidade",
        "preco_unitario",
        "idade",
        "mes"
    ]
]

# Variável alvo
y = dados["valor_total"]

# Divisão treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Carregar modelo treinado
with open("../model/modelo.pkl", "rb") as arquivo:
    modelo = pickle.load(arquivo)

# Realizar previsões
predicoes = modelo.predict(X_test)

# Calcular métricas
rmse = mean_squared_error(
    y_test,
    predicoes
) ** 0.5

r2 = r2_score(
    y_test,
    predicoes
)

# Exibir resultados
print("\n===== AVALIAÇÃO DO MODELO =====")
print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.4f}")

# Comparação entre valores reais e previstos
resultado = pd.DataFrame({
    "Valor Real": y_test.values,
    "Valor Previsto": predicoes.round(2)
})

print("\nAmostra de previsões:")
print(resultado.head(10))

# Salvar resultados
resultado.to_csv(
    "../resultados/previsoes.csv",
    index=False
)

print("\nArquivo previsoes.csv salvo na pasta resultados.")