import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Carregar dataset preparado
dados = pd.read_csv("../datasets/dataset_features.csv")

# Variáveis de entrada (features)
X = dados[
    [
        "quantidade",
        "preco_unitario",
        "idade",
        "mes"
    ]
]

# Variável alvo (target)
y = dados["valor_total"]

# Divisão entre treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Criação do modelo
modelo = LinearRegression()

# Treinamento
modelo.fit(X_train, y_train)

# Salvar o modelo treinado
with open("../model/modelo.pkl", "wb") as arquivo:
    pickle.dump(modelo, arquivo)

print("Modelo treinado e salvo com sucesso.")
print(f"Registros para treino: {len(X_train)}")
print(f"Registros para teste: {len(X_test)}")