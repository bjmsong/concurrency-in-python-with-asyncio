import socket

"""
telnet localhost 8000
"""

# create a server socket
# AF_INET: type of address will be able to interact with
# SOCK_STREAM: use TCP protocol
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# client can use this address to send data to server
server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()

# block until getting a connection
# connection: socket object
connection, client_address = server_socket.accept()
print(f'I got a connection from {client_address}!')
server_socket.close()


