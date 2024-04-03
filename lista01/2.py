# 2. Escreva uma função recursiva para calcular o fatorial de um número. 

def fatorial (n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fatorial (n-1)
    
numero = 5
resposta = fatorial(numero)
print(f'O fatorial de {numero} é igual a {resposta}')

# Esse f no print é uma forma de formatação de strings com tipos númericos em python, funciona muito bem.

# q: Na função recursiva, acontece o seguinte:
# a: 5 * fatorial(4) | 4 * fatorial(3) | 3 * fatorial(2) | 2 * fatorial(1) | 1 * fatorial(0) | 1





