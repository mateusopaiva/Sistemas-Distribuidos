import socket

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 2424

MULTICAST_TTL = 2

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

sock.sendto(b"Hello World!", (MCAST_GRP, MCAST_PORT))