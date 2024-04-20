# Escreva um programa Python onde uma thread gera números aleatórios entre 1 e 100 e os coloca em uma fila. Outra thread retira esses números da fila e os imprime na tela. Certifique-se de que a fila esteja sendo manipulada de forma segura para evitar problemas de concorrência
#####
# O programa pode ser executado com o comando: python3 ex03.py
import threading
import multiprocessing
import queue
import random

fila = queue.Queue()

eventT1 = threading.Event()
eventT2 = threading.Event()

def gerarNumeros(name):
    for _ in range(100):
        num = random.randint(1, 100)
        fila.put(num)
        print(f'{name} gerou o número {num}')
        # Sinaliza a t2 que o número foi gerado e está pronto para ser impresso
        eventT1.set() 

        # t1 aguarda a t2 imprimir o número. Isso faz a t1 esperar t2 até ela sinalizar que imprimiu o número
        eventT2.wait() 

        # t1 então torna t2 como não definido, para que ela possa ser sinalizada novamente
        eventT2.clear()

def imprimirNumeros (name):
    for _ in range(100): # Imprime o primeiro número na fila, nessa execução

        # t2 está aguardando t1 gerar o primeiro número antes de ter alguma coisa para imprimir (eventT1.wait = esperando o evento t1 acontecer)
        eventT1.wait()

        # t2 imprime, pois na função gerarNumeros, o evento t1 foi sinalizado com o eventT1.set()
        print(f'{name} imprimiu o número: {fila.get()}')

        # t2 torna o eventT1 como não definido, o preparando para que a t1 possa sinalizar novamente
        eventT1.clear()

        # t2 sinaliza a t1 que o número foi impresso
        eventT2.set()

t1 = threading.Thread(target=gerarNumeros, args=('t1',))
t2 = threading.Thread(target=imprimirNumeros, args=('t2',))

t1.start()
t2.start()

t1.join()
t2.join()

print (f'Fim do programa')

