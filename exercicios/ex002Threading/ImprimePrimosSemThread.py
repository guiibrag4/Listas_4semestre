import os

num_cores = os.cpu_count()
print(f"O número de cores do processador é: {num_cores}")

# ImprimePrimosSemThread.py

def ehPrimo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def imprimePrimos():
    for i in range(100000):
        if ehPrimo(i):
            print(i)
            
imprimePrimos()

# O código acima imprime todos os números primos de 0 a 100000. O problema é que ele é muito lento. Vamos tentar paralelizar a execução dele.

# cd Listas de exercício/exercicios/ex002Threading
# measure-command { python ImprimePrimosSemThread.py | Out-Default }
