# UDP socket sending sample (for receiver sample see `udp_recv.py`)
import socket

HOST = 'localhost'
PORT = 12345

message = b'Hello, from UDP!'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(message, (HOST, PORT))
sock.close()  # we are done
