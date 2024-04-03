# Explicações no final do código
import numpy as np

def transposta(matriz):
    return matriz.T
  
vetor = np.array [[1,2,3]
                  [4,5,6]
                  [7,8,9]]

matriz_transposta = transposta(vetor)
print (f'A matriz transposta é: \n{matriz_transposta}')

# Esse atributo ".T" é responsável por trocar as linhas de uma matriz por colunas ou vice-versa.

# O numpy, sendo utilizado novamente, para trabalhar rapidamente e efetivamente com vetores

# Dai, nada demais, cria uma variável "matriz_transposta" e passa o vetor como parâmetro da função, depois disso, a função é realizada "return matriz.T" e o código imprime a varíavel que armazenou o return da função.
