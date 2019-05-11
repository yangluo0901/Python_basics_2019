import socket  # python pyi file, similar with interface

HOST = "localhost"
PORT = 6969

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:  # socket.pyi -> socket. class
    server.bind(("", PORT))
    server.listen()
    print("Ready to accept")
    connection, address = server.accept()
    with connection:
        print("Connection established, connection is {} ,\n  address is {}".format(connection, address))
        while True:
            data = connection.recv(1024)
            if not data:
                print("End of Message !")
                break
            print("Message recieved : ", data)
        connection.send("message recieved".encode())
