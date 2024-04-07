#ImprimePrimos2Threads.py

import threading
import os

num_cores = os.cpu_count()
print(f"O número de cores do processador é: {num_cores}")

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
            
t1 = threading.Thread(target=imprimePrimos)
t2 = threading.Thread(target=imprimePrimos)

t1.start()
t2.start()

t1.join()
t2.join()


     

