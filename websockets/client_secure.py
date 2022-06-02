#!/usr/bin/env python

"""Secure WebSocket client from [Encrypt connections](https://websockets.readthedocs.io/en/stable/intro/quickstart.html#encrypt-connections) tutorial
usage: client_secure.py [certificate.pem]

test:
- run server_secure.py
- run client_secure.py
"""

import asyncio
import pathlib
import ssl
import websockets
import sys


async def main(args):
	cert_file = 'localhost.pem'
	if len(args) > 1:
		cert_file = args[1]

	print('certificate: ', cert_file)

	ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
	cert_pem = pathlib.Path(__file__).with_name(cert_file)
	ssl_context.load_verify_locations(cert_pem)

	uri = "wss://localhost:8765"
	async with websockets.connect(uri, ssl=ssl_context) as websocket:
		msg = input("Something to say? ")
		
		await websocket.send(msg)
		print(f">>> {msg}")

		answer = await websocket.recv()
		print(f"<<< {answer}")

		print('done!')

if __name__ == "__main__":
	asyncio.run(main(sys.argv))
