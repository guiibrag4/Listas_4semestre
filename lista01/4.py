import numpy as np

def transposta_matriz(matriz):
    transposta = np.transpose(matriz)
    return transposta

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz_transposta = transposta_matriz(matriz)
print("Matriz original:")
print(matriz)
print("Matriz transposta:")
print(matriz_transposta)
