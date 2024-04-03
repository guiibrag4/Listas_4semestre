# O problema da variação 1 é que o chute para as 2 threads tem o mesmo chute inicial, o que faz com que as threads tenham o mesmo comportamento. Por isso, quem vai encontrar primeiro é a thread 1. Nessa variação, uma thread procurara por números pares e a outra por números ímpares.

import random
import threading
from datetime import datetime

numero_sorteado = 0
numero_encontrado = False
numero_maximo = 1000

def gerarNumeroAleatorio():
    global numero_sorteado
    numero_sorteado = random.randint(1, numero_maximo)
    print(f'Número sorteado: {numero_sorteado}')

def descobrirNumeroGerado(nome, controle):
    global numero_sorteado
    global numero_encontrado
    chute_inicial = int(numero_maximo/2) #Casting para sempre gerar um inteiro
    chute = chute_inicial
    if (controle):
        chute = chute_inicial + 1

    while not numero_encontrado:
        print(f'{nome} está chutando o número: {chute}')
        if chute < numero_sorteado:
            chute+=2
        elif chute > numero_sorteado:
            chute-=2
        else:
            numero_encontrado = True
            print(f'Número encontrado pela thread: {nome}')
            # print(f'Número encontrado pela thread: {threading.current_thread().name}) # Segunda forma de printar o nome da thread
            break

def main ():
    gerarNumeroAleatorio()

     # Segunda forma de nomear thread1 = threading.Thread(target=descobrirNumeroGerado, args=('Thread 1', name='Thread 1'))
    thread1 = threading.Thread(target=descobrirNumeroGerado, args=('Thread 1', True,))
    thread2 = threading.Thread(target=descobrirNumeroGerado, args=('Thread 2', False,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

inicio = datetime.now()
if __name__ == '__main__':
    main()
    print(f'Tempo de execução: {datetime.now() - inicio}')

            
