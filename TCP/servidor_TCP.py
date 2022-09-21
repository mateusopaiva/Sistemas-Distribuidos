import socket

HOST = 'localhost'    
PORT = 5000            

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

socketTCP.bind(orig)
socketTCP.listen(1)

try:
    while True:
        conexao, cliente = socketTCP.accept()
        print ('Concetado por', cliente)
        conexao.send (str.encode ("Conexão com o servidor esta funcionado"))

        while True:
            msg = str(conexao.recv(1024).decode('utf8'))
            if not msg: break
            print (cliente, msg)
        print ('Finalizando conexao com o cliente', cliente)
        conexao.close()
except:
        conexao.close()