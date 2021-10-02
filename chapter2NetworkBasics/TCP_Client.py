import socket
target_host = "127.0.0.1"
target_port = 9999

#-Create a socket object
# -AF_INET is saying we are going to use ipv4
# -SOCK_STREAM is saying we are using TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#We then connect to the client
client.connect((target_host, target_port))

while True:
    #The Message we are sending
    msg = input()

    #This encodes the message so it can be sent
    byte = msg.encode()
    #print(byte)

    #This Sends the data
    client.send(byte)

    #This Listens for a response
    response = client.recv(4096)
    response = response.decode()

    #And Prints the response
    print(response)