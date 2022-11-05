import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:2424")

while True:
    op = []
    message = socket.recv_string()
    op.append(message)
    socket.send_string("Operacao de %s" % message)
    time.sleep(1)

    if op[0] == 'soma':
        message = socket.recv_string()
        numero = int(message)
        op.append(numero)
        socket.send_string("Primeiro numero adicionado, Adicione o outro numero ")
        time.sleep(1)
        message = socket.recv_string()
        numero = int(message)
        op.append(numero)

        soma = op[1] + op[2]
        numero = str(soma)

        socket.send_string(numero)

    if op[0] == 'sub':
        message = socket.recv_string()
        numero = int(message)
        op.append(numero)
        socket.send_string("Primeiro numero adicionado, Adicione o outro numero ")
        time.sleep(1)

        message = socket.recv_string()
        numero = int(message)
        op.append(numero)

        sub = op[1] - op[2]
        numero = str(sub)
        socket.send_string(numero)

    if op[0] == 'mult':
        message = socket.recv_string()
        numero = int(message)
        op.append(numero)
        socket.send_string("Primeiro numero adicionado, Adicione o outro numero ")
        time.sleep(1)

        message = socket.recv_string()
        numero = int(message)
        op.append(numero)

        mult = op[1] * op[2]
        numero = str(mult)
        socket.send_string(numero)