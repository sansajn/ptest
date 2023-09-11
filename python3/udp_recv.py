# receive UDP socket data sample (for sender sample see `udp_recv.py`)
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = 'localhost'
PORT = 12345

sock.bind((HOST, PORT))

print(f'Listening on {HOST}:{PORT} ...')  # TODO: spoznamkujsi toto do python_tips

while True:
	try:
		data, sender_addr = sock.recvfrom(4*1024)
		print(f"{sender_addr} >> {data.decode('utf-8')}")
	
	except KeyboardInterrupt:
		print("terminated by user")
		break

sock.close()
