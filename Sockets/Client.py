import socket

HOST = "localhost"
PORT = 6969
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    message = input("type message:")
    client.send(message.encode())
    reply_message = client.recv(1024)
print("Server replies : {}".format(reply_message))

