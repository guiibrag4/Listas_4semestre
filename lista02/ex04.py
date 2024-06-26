# Desenvolva um programa Python que crie 5 threads, cada uma realizando uma operação de espera (sleep)aleatória entre 1 e 5 segundos. Imprima uma mensagem quando cada thread iniciar e quando terminar. Certifique-se de que o programa espere todas as threads terminarem antes de imprimir a
# mensagem de conclusão.

import threading
import random
import time

def ThreadTimeRandom (identificador):
    duracao = random.randint(1, 5)
    print (f'Thread {identificador} iniciada. Tempo de espera: {duracao} segundos.')
    time.sleep(duracao)
    print(f'Thread {identificador} finalizada!')

threads = []

for i in range (5):
    thread = threading.Thread(target=ThreadTimeRandom, args=(i+1,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print ('Todas as threads terminaram a sua execução.')
