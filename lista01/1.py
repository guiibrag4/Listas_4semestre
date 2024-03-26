import numpy as np

def ordenar_vetor(vetor):
    vetor_ordenado = np.sort(vetor)
    return vetor_ordenado

vetor = np.array([3, 1, 4, 1, 5, 9, 2, 6])
vetor_ordenado = ordenar_vetor(vetor)
print("Vetor ordenado:", vetor_ordenado)
