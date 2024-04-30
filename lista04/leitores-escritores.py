'''
Desenvolva um programa em Python que simule o problema dos leitores e 
escritores. Tenha uma variável compartilhada que represente um recurso que 
pode ser lido e escrito. Vários leitores podem ler o recurso simultaneamente, mas 
apenas um escritor pode escrever nele por vez. Utilize semáforos para controlar o 
acesso ao recurso e garantir que não ocorra condição de corrida entre leitores e 
escritores.
'''

import threading

novaYork_news = 0

# Semáforos
sem = threading.Semaphore(5) # 5 leitores podem ler ao mesmo tempo
mutex = threading.Lock() #Semáforo binário, com "down" e "up" (Ações atômicas, que garantem que quando uma operação está sendo executada no semáforo, nenhum processo pode acessar o semáforo)

def leitor(nome):
    global novaYork_news
    sem.acquire()
    print(f'Leitor {nome} está lendo a notícia: {novaYork_news}')
    sem.release()

def escritor (nome):
    global novaYork_news
    mutex.acquire()
    novaYork_news += 1
    print (f'Escritor {nome} está escrevendo a notícia: {novaYork_news}')
    mutex.release()
    print ()
    
threads = []
for i in range(5):
    t = threading.Thread(target=leitor, args=(f'{i+1}',))
    threads.append(t)
    t.start()
    
    t = threading.Thread(target=escritor, args=(f'{i+1}',))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

'''
acquire() é usado para solicitar o semáforo. Se o valor interno do semáforo for maior que zero, então ele é decrementado e a execução continua. Se o valor interno for zero, acquire() bloqueia e espera até que algum outro thread chame release().

release() é usado para liberar o semáforo. Quando release() é chamado, o valor interno do semáforo é incrementado. Se houver threads esperando para adquirir o semáforo, um deles conseguirá e sua execução continuará.

'''
