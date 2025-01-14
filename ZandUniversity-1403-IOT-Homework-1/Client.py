import socket

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))  # Server address and port

try:
    while True:
        # Send message to server
        message = input(" Client : ")
        client_socket.sendall(message.encode())

        if data := client_socket.recv(1024).decode():
            print(" Server : ", data)

        else:
            break
finally:
    client_socket.close()