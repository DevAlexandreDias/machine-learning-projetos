import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Gerando dados simulados de transações financeiras
np.random.seed(42)

# 950 transações legítimas (0) e 50 fraudulentas (1)
n_legitimas = 950
n_fraudes = 50

valor_legitimo = np.random.normal(loc=150, scale=50, size=n_legitimas)
valor_fraude = np.random.normal(loc=1200, scale=300, size=n_fraudes)

dispositivo_novo_legitimo = np.random.choice([0, 1], size=n_legitimas, p=[0.9, 0.1])
dispositivo_novo_fraude = np.random.choice([0, 1], size=n_fraudes, p=[0.2, 0.8])

tentativas_senha_legitimo = np.random.choice([1, 2], size=n_legitimas, p=[0.95, 0.05])
tentativas_senha_fraude = np.random.choice([1, 2, 3], size=n_fraudes, p=[0.2, 0.5, 0.3])

# Montando o DataFrame
df_legitimas = pd.DataFrame({
    'valor_transacao': valor_legitimo,
    'dispositivo_novo': dispositivo_novo_legitimo,
    'tentativas_senha': tentativas_senha_legitimo,
    'e_fraude': 0
})

df_fraudes = pd.DataFrame({
    'valor_transacao': valor_fraude,
    'dispositivo_novo': dispositivo_novo_fraude,
    'tentativas_senha': tentativas_senha_fraude,
    'e_fraude': 1
})

df = pd.concat([df_legitimas, df_fraudes]).sample(frac=1, random_state=42).reset_index(drop=True)

x = df[['valor_transacao', 'dispositivo_novo', 'tentativas_senha']]
y = df['e_fraude']


x_trein, x_test, y_trein, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)


rf = RandomForestClassifier(
    n_estimators=100, 
    class_weight='balanced',  # Penaliza mais os erros na classe minoritária (Fraude)
    random_state=42
)
rf.fit(x_trein,y_trein)
previsoes = rf.predict(x_test)

print("=== RELATÓRIO DE CLASSIFICAÇÃO ===")
print(classification_report(y_test, previsoes, target_names=['Legítima', 'Fraude']))

print("\n=== MATRIZ DE CONFUSÃO ===")
cm = confusion_matrix(y_test, previsoes)
print(cm)

# 5. Extração e exibição do Feature Importance
importancias = rf.feature_importances_
colunas = x.columns

df_importancia = pd.DataFrame({
    'Variavel': colunas,
    'Importancia': importancias
}).sort_values(by='Importancia', ascending=False)

print("\n=== IMPORTÂNCIA DAS VARIÁVEIS (FEATURE IMPORTANCE) ===")
print(df_importancia)

