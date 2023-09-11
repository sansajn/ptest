#!/usr/bin/env python

"""Secure WebSocket server from [Encrypt connections](https://websockets.readthedocs.io/en/stable/intro/quickstart.html#encrypt-connections) tutorial
usage: echo_secure [certificate.pem]

testing:
- run server_secure.py
- run client_secure.py
"""

import asyncio
import pathlib
import ssl
import websockets
import sys

async def hello(websocket, path):
	msg = await websocket.recv()
	print(f"<<< {msg}")
	
	await websocket.send(msg)
	print(f">>> {msg}")

async def main(args):
	cert_file = 'localhost.pem'
	if len(args) > 1:
		cert_file = args[1]

	ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
	cert_pem = pathlib.Path(__file__).with_name(cert_file)
	ssl_context.load_cert_chain(cert_pem)

	print('listenning on wss://localhost:8765 address')
	async with websockets.serve(hello, "localhost", 8765, ssl=ssl_context):
		await asyncio.Future()  # run forever

if __name__ == "__main__":
	asyncio.run(main(sys.argv))
