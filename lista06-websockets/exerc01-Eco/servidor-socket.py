import socket
import threading

# Definindo o endereço IP e a porta
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 12345        # Porta que o servidor está escutando

def handle_client(conn, addr):
    print(f"Nova conexão: {addr}")
    while True:
        # Recebendo a mensagem do cliente
        msg = conn.recv(1024).decode('utf-8')
        if not msg:
            break
        print(f"Recebido de {addr}: {msg}")
        # Enviando a mesma mensagem de volta ao cliente (eco)
        conn.sendall(msg.encode('utf-8'))
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Servidor escutando em {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()