import threading
import time
import random

def trabalho(identificador):
    duracao = random.randint(1, 5)
    print(f"Thread {identificador} iniciada. Tempo de espera: {duracao} segundos.")
    time.sleep(duracao)
    print(f"Thread {identificador} terminada.")

threads = []

for i in range(5):
    thread = threading.Thread(target=trabalho, args=(i+1,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Todas as threads terminaram. Programa finalizado.")
