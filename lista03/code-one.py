# A lista 3 se resume em: Ler o slide completo e estuda-lo, após isso, reecriar o código do slide e entender a lógica e os métodos por detrás dele.

import threading

def processar_parte (nome, lista, inicio, fim):
    for i in range (inicio,fim):
        print (f'{nome} - Item {i} - Valor {lista[i]}')
        lista[i] = lista[i] * 2
        
def processamento_multitarefa(lista):
    tamanho = len(lista)
    meio = tamanho // 2
    
    t1 = threading.Thread(target=processar_parte, args=("Thread1", lista, 0, meio))
    t2 = threading.Thread(target=processar_parte, args=("Thread2", lista, meio, tamanho))
    
    print ('Start 1')
    t1.start()
    print ('Start 2')
    t2.start()
    
    t1.join()
    t2.join()
    
def main ():
    processamento_multitarefa([14,-29,345,4430,532,612.32,723,2121,478,-180])
    
if __name__ == '__main__':
    main()
    
    