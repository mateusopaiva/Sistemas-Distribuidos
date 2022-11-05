import time
import zmq

contex = zmq.Context()
socket = contex.socket(zmq.PUB)
socket.bind("tcp://*:5555")

while True:
    time.sleep(1)
    socket.send(b"Entretenimento")
    socket.send(b"Economia")
    socket.send(b"Esportes")
    socket.send(b"Politica")
    socket.send(b"Bem-estar")