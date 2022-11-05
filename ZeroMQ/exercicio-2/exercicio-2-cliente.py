import zmq

context = zmq.Context()

print("Conectando no servidor …")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:2424")

while True:
    message = input("\nDigite uma operacao: (soma, sub, mult) ")
    socket.send_string(message)
    message = socket.recv_string()
    print("[ %s ]" % message)

    message = input("Digite o primeiro valor: ")
    socket.send_string(message)
    message = socket.recv_string()
    print("[ %s ]" % message)

    message = input("Digite o segundo valor: ")
    socket.send_string(message)

    message = socket.recv_string()
    resultado = int(message)
    print("[Resultado = %d ]" % resultado)