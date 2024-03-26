def contar_numeros(vetor):
    positivos = sum(1 for num in vetor if num > 0)
    negativos = sum(1 for num in vetor if num < 0)
    zeros = sum(1 for num in vetor if num == 0)
    return positivos, negativos, zeros

def ler_vetor():
    vetor = []
    tamanho = int(input("Digite o tamanho do vetor: "))
    for i in range(tamanho):
        elemento = int(input(f"Digite o {i+1}º número inteiro: "))
        vetor.append(elemento)
    return vetor

vetor = ler_vetor()
positivos, negativos, zeros = contar_numeros(vetor)
print("Quantidade de números positivos:", positivos)
print("Quantidade de números negativos:", negativos)
print("Quantidade de zeros:", zeros)
