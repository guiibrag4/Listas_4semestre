import socket
import threading

# Definindo o endereço IP e a porta
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 12345        # Porta que o servidor está escutando

# Lista para armazenar os clientes conectados
clientes = []
nicknames = []

def broadcast(message, _client):
    for client in clientes:
        if client != _client:
            client.sendall(message)

def handle_client(client):
    while True:
        try:
            # Recebendo a mensagem do cliente
            msg = client.recv(1024)
            broadcast(msg, client)
        except:
            index = clientes.index(client)
            clientes.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f'{nickname} deixou o chat!'.encode('utf-8'), _client=None)
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Servidor escutando em {HOST}:{PORT}")
    while True:
        client, addr = server.accept()
        print(f"Nova conexão: {addr}")
        clientes.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    start_server()