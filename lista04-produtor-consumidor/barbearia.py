'''
Modele o problema da barbearia com múltiplos barbeiros utilizando threads em 
Python. Tenha um número fixo de cadeiras na barbearia e um número variável de 
barbeiros. Os clientes chegam à barbearia e verificam se há cadeiras disponíveis. 
Se todas as cadeiras estiverem ocupadas, eles saem; caso contrário, eles 
ocupam uma cadeira e aguardam serem chamados por um barbeiro. Os 
barbeiros, quando disponíveis, chamam o próximo cliente e o atendem. Utilize 
semáforos para controlar o acesso às cadeiras e garantir a exclusividade do 
atendimento.
'''

import threading
import time
import random

CADEIRAS = 5 # Maiúsculo pq é constante
barbeiros = 0
clientes = 10

cadeiras_ocupadas = 0
cadeiras_livres = threading.Semaphore (CADEIRAS)
mutex = threading.Lock()

def barbeiro(i):
    global barbeiros, cadeiras_ocupadas
    with mutex:
        barbeiros -= 1
    print(f'Barbeiro {i} está cortando cabelo de um cliente')
    time.sleep(random.randint(1, 3))
    print(f'Barbeiro {i} terminou de cortar o cabelo desse cliente')

def cliente(i):
    global cadeiras_ocupadas
    with mutex:
        if cadeiras_ocupadas < CADEIRAS:
            cadeiras_ocupadas += 1
            print(f'Cliente {i} sentou em uma cadeira e está esperando um barbeiro')
            cadeiras_livres.release()
        else:
            print(f'Cliente {i} não encontrou cadeiras disponíveis e foi embora')

print ('Barbearia aberta! Quantos barbeiros terá na sua barbearia?')
barbeiros = int(input())

for i in range (barbeiros):
    threading.Thread(target=barbeiro, args=(i,)).start()

for i in range(clientes):
    threading.Thread(target=cliente, args=(i,)).start()
