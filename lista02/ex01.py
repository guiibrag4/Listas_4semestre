import threading

def imprimir_numeros(nome):
    for i in range(1, 6):
        print(nome, i)

thread1 = threading.Thread(target=imprimir_numeros, args=("Thread 1:",))
thread2 = threading.Thread(target=imprimir_numeros, args=("Thread 2:",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Programa finalizado.")
