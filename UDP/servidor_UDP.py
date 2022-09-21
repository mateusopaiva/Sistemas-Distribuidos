import socket

localIP     = "localhost"
localPort   = 20001
bufferSize  = 1024

msgFromServer = "Cliente conectado via UDP"
bytesToSend = str.encode(msgFromServer)

# Cria um UDP/IP socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Associa o socket à uma porta
UDPServerSocket.bind((localIP, localPort))

#print("Servidor em funcionamento")
while(True):

    # Recebe dados de um socket e, retorna a tupla (string, address)
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = str(bytesAddressPair[0].decode('utf8'))
    address = bytesAddressPair[1]

    clientIP  = "Endereço de IP do Cliente: {}".format(address)
    clientMsg = "Mensagem do Cliente: {}\n".format(message)
    print(clientIP)
    print(clientMsg)

    UDPServerSocket.sendto(bytesToSend, address)