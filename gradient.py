import numpy as np 
import matplotlib.pyplot as plt

X = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])
b = 0.0
w = 0.0
alpha = 0.01
repetição = 1000

n = float(len(X))


for i in range (repetição):
    y_pred = w * X + b
    custo = (1/n) * sum((y-y_pred)**2)

    dw = (-2/n) * sum(X*(y-y_pred))
    db = (-2/n) * sum((y-y_pred))


    w = w - alpha * dw
    b = b - alpha * db

    if i % 100 == 0:
        print(f"Época {i}: Custo = {custo:.2f} | w = {w:.2f}, b = {b:.2f}")

print(f"\nValores finais após o treino -> w: {w:.2f}, b: {b:.2f}")


plt.plot(X, y_pred, color="red", linewidth=3, label="Linha do Gradiente")

# Customização do gráfico
plt.title("Resultado Final do Gradiente Descendente")
plt.xlabel("X")
plt.ylabel("y")
plt.ylim(0, 14)
plt.legend()
plt.grid(True)

# Abre a janela do Matplotlib na tela
plt.show()