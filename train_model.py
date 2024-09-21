from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
import joblib

# Gerar dados de exemplo para treino
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)

# Separar os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Salvar o modelo usando joblib
joblib.dump(model, "linear_regression_model.pkl")

print("Modelo treinado e salvo com sucesso!")
