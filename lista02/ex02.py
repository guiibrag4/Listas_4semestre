import threading

variavel_global = 0
lock = threading.Lock()

def incrementar(nome):
    global variavel_global
    for _ in range(500):
        with lock:
            variavel_global += 1
            print(f"{nome}: {variavel_global}")

# O python não entende que 'variavel_global' é uma variável criada globalmente, por isso é necessário declarar a variável como global dentro da função, para ela não criar uma variável localmente.

thread1 = threading.Thread(target=incrementar, args=('Thread1',))
thread2 = threading.Thread(target=incrementar, args=('Thread2',))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Valor final da variável global:", variavel_global)
