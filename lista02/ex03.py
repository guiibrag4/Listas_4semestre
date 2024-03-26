import threading
import queue
import random
import time

fila = queue.Queue()

def adicionar_numeros():
    while True:
        numero = random.randint(1, 100)
        fila.put(numero)
        print("Número adicionado à fila:", numero)
        time.sleep(1)  

def imprimir_numeros():
    while True:
        if not fila.empty():
            numero = fila.get()
            print("Número retirado da fila:", numero)
        time.sleep(2) 

thread_adicionar = threading.Thread(target=adicionar_numeros)
thread_imprimir = threading.Thread(target=imprimir_numeros)

thread_adicionar.start()
thread_imprimir.start()

thread_adicionar.join()
thread_imprimir.join()
