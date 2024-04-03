import numpy as np

def ordenar_valor (vetor1):
    ordened = np.sort(vetor1)
    return ordened
    
vetor = np.array([10, 30, 20, 15, 19, 32, 35, 25, 2])
vetor_ordernado = ordenar_valor(vetor)
print(f'O vetor ordenado é: {vetor_ordernado}')


# O código define uma função chamada ordenar_vetor que recebe um vetor e retorna o vetor ordenado. A função utiliza a função np.sort do NumPy para ordenar o vetor. Em seguida, o código cria um vetor de números inteiros e chama a função ordenar_vetor passando o vetor como argumento. Por fim, o código imprime o vetor ordenado. O código ordena o vetor de forma crescente.

# O método np.sort ordena um vetor de forma crescente.
# O método np.array converte uma lista em um vetor do NumPy.
# A conversão de uma lista em um vetor do NumPy permite utilizar funções do NumPy, como a função np.sort, que não estão disponíveis para listas comuns do Python.

