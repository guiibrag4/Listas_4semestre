import threading

variavel_global = 0

def incrementar():
    global variavel_global
    for _ in range(100):
        variavel_global += 1

thread1 = threading.Thread(target=incrementar)
thread2 = threading.Thread(target=incrementar)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Valor final da variável global:", variavel_global)
