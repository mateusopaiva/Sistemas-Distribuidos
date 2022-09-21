import socket

serverAddressPort   = ('localhost', 20001)
bufferSize          = 1024

msgFromClient       = 'Servidor em funcionamento'
bytesToSend         = str.encode(msgFromClient)

#cria um UDP/IP socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Recebe como parâmetros a mensagem e o endereço.
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

# Recebe dados de um socket e, retorna a tupla (string, address)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = str('Mensagem do Servidor: {}\n'.format(str(msgFromServer[0].decode('utf8'))))
print(msg)

while(msgFromClient != 'q'):

    msgFromClient = input('Cliente: ')
    bytesToSend = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)