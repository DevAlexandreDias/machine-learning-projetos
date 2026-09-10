import numpy as np 
import matplotlib.pyplot as plt


x = np.array([[40, 50, 60, 70, 80, 90, 100, 110, 120]])
y = np.array([180000, 210000, 260000, 310000, 350000, 410000, 440000, 500000, 530000])

media_x = np.mean(x)
media_y = np.mean(y)

numerador = np.sum((x-media_x) * (y - media_y))
denominador = np.sum((x-media_x)**2)

a = numerador / denominador
b = media_y - (a * media_x)

print(f"Coeficiente angular (a): {a}")
print(f"Coeficiente linear (b): {b}")
print(f"Equação da reta: y = {a}x + {b}")

def prever(valor_x):
    return a * valor_x + b

tamanho_novo = 85
previsao = prever(tamanho_novo)
print(f"Previsão do preço para o tamanho {tamanho_novo}: {previsao}")

plt.scatter(x, y, color='blue', label='Dados Reais')
plt.plot(x, a * x + b, color='red', label='Reta de Regressão')
plt.xlabel('Tamanho (m²)')
plt.ylabel('Preço (R$)')
plt.legend()
plt.grid(True)
plt.show()
