import socket

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))  # Server address and port
server_socket.listen(1)
print(" The server is listening... ")

#  Waiting for client connection
conn, addr = server_socket.accept()
print(" Client connected : ", addr)

try:
    while True:
        # Receive messages from the client
        data = conn.recv(1024).decode()
        if not data:
            break
        print(" Client : ", data)
        
        # Send response to client
        message = input(" Server : ")
        conn.sendall(message.encode())

finally:
    conn.close()
    server_socket.close()