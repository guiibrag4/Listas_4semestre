import socket
import threading

# Definindo o endereço IP e a porta
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 12345        # Porta que o servidor está escutando

# Criando um socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            # Recebendo a mensagem do servidor
            msg = client.recv(1024).decode('utf-8')
            print(msg)
        except:
            # Fechando a conexão quando ocorrer um erro
            print("Erro!")
            client.close()
            break

def write():
    while True:
        # Enviando uma mensagem para o servidor
        msg = f'{nickname}: {input("")}'
        client.send(msg.encode('utf-8'))

# Escolhendo um nickname
nickname = input("Escolha um nickname: ")

# Iniciando threads para escutar e enviar mensagens
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()