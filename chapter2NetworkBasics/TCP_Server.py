import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print("[*] Listing on %s:%d" % (bind_ip, bind_port))




def handelClient(clientSocket):

    recived = clientSocket.recv(1024).decode()
    print("[*] Recived: %s" % recived)

    clientSocket.send(("ACK!").encode())

    recived = clientSocket.recv(1024).decode()
    print("[*] Recived: %s" % recived)


    clientSocket.close()

def custom_handel(clientSocket):
    while True:
        recived = clientSocket.recv(1024).decode()
        print("[*] Recived: %s" % recived)

        clientSocket.send(("ACK!").encode())







while True:
    client, addr = server.accept()
    print("[*] Accepted connection from %s:%d" % (addr[0], addr[1]))

    clientHandler = threading.Thread(target=custom_handel, args=(client,))
    clientHandler.start()

