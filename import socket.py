import socket
import threading

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message:
            print(f"Received message: {message}")
            # Broadcast message to all connected clients
            for client in clients:
                if client != client_socket:
                    client.send(message.encode('utf-8'))
        else:
            break
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5555))
server.listen(5)

clients = []
print("Server is listening...")

while True:
    client_socket, addr = server.accept()
    print(f"Accepted connection from {addr}")
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket,)).start()
