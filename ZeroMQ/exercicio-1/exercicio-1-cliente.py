from email import message
from multiprocessing import context
from socket import socket
import zmq

context = zmq.Context()

print("Conectando ao Servido ...\n")

socketEconomia = context.socket(zmq.SUB)
socketEconomia.connect("tcp://localhost:5555")
socketEconomia.setsockopt(zmq.SUBSCRIBE, b"Economia")

socketEntretenimento = context.socket(zmq.SUB)
socketEntretenimento.connect("tcp://localhost:5555")
socketEntretenimento.setsockopt(zmq.SUBSCRIBE, b"Entretenimento")

socketEsportes = context.socket(zmq.SUB)
socketEsportes.connect("tcp://localhost:5555")
socketEsportes.setsockopt(zmq.SUBSCRIBE, b"Esportes")

socketPolitica = context.socket(zmq.SUB)
socketPolitica.connect("tcp://localhost:5555")
socketPolitica.setsockopt(zmq.SUBSCRIBE, b"Politica")

socketBemEstar = context.socket(zmq.SUB)
socketBemEstar.connect("tcp://localhost:5555")
socketBemEstar.setsockopt(zmq.SUBSCRIBE, b"Bem-estar")

while True:
    topicoEconomia = socketEconomia.recv()
    topicoEntretenimento = socketEntretenimento.recv()
    topicoEsportes = socketEsportes.recv()
    topicoPolitica = socketPolitica.recv()
    topicoBemEstar = socketBemEstar.recv()

    
    print(f"Manchete de Economia: {topicoEconomia}\n")
    print(f"Manchete de Entretenimento: {topicoEntretenimento}\n")
    print(f"Manchete de Esportes: {topicoEsportes}\n")
    print(f"Manchete de Politica: {topicoPolitica}\n")
    print(f"Manchete de Bem-estar: {topicoBemEstar}\n")