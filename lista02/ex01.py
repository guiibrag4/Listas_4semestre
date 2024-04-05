import threading

def numeros (nome):
    for i in range(1,15):
        print(f"{nome}: {i}")

thread1 = threading.Thread(target=numeros, args=('Thread1',))
thread2 = threading.Thread(target=numeros, args=('Thread2',))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print ('\nPrograma encerrado')



# threading.Thread(target=funcao, args=(argumentos,)) -> cria uma thread. O target indica a função que será executada pela thread e args são os argumentos da função.

# thread.start() -> inicia a thread.

# thread1.join() e thread2.join(): Estas linhas estão fazendo o programa principal esperar até que as threads terminem. O método join() bloqueia a execução do programa principal até que a thread em que é chamado termine. Isso é útil se você quiser garantir que uma thread termine antes de continuar a execução do programa principal.
