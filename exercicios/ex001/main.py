import threading 

def processar_parte(processo,lista, inicio,fim):
    for i in range(inicio,fim):
      print(str(processo)+" "+str(i))
      lista[i]= lista[i] * 2
      
    # q: qual o valor inicial desse i e qual será seu valor após a primeira execução do loop?
      # a: i = inicio, após a primeira execução do loop i = inicio + 1
   #  q: e se eu quisesse incrementar o i de 2 em 2, como deveria ficar o loop?
      # a: for i in range(inicio,fim,2):
   
def processamento_multitarefa(lista):
   tamanho = len(lista)
   meio = int(tamanho/2)
   t1 = threading.Thread(target=processar_parte,args=(1,lista,0,meio)) 
   t2 = threading.Thread(target=processar_parte,args=(2,lista,meio,tamanho))    
   print("Inicio Thread 1")
   t1.start()  
   print("Inicio Thread 2")
   t2.start()

   t1.join()
   t2.join()

lista_numeros = list(range(1,101))

processamento_multitarefa(lista_numeros)