import socket

HOST = 'localhost'     
PORT = 5000 

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

socketTCP.connect(dest)

servidor_msg = socketTCP.recv(1024).decode('utf8')                    
print(servidor_msg)   

print('Digite sua mensagem ou aperte a letra q para finalizar:')
msg = input() 
while(True):
    if(msg == 'q'):
        break
    socketTCP.send (str.encode(msg))
    msg = input()
print ('Conexao com o servidor foi finalizada', )
socketTCP.close()