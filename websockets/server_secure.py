#!/usr/bin/env python

"""Secure WebSocket server from [Encrypt connections](https://websockets.readthedocs.io/en/stable/intro/quickstart.html#encrypt-connections) tutorial
"""

import asyncio
import pathlib
import ssl
import websockets

async def hello(websocket, path):
	name = await websocket.recv()
	print(f"<<< {name}")

	greeting = f"Hello {name}!"
	await websocket.send(greeting)
	print(f">>> {greeting}")


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_cert_chain(localhost_pem)

async def main():
	async with websockets.serve(hello, "localhost", 8765, ssl=ssl_context):
		await asyncio.Future()  # run forever

if __name__ == "__main__":
	asyncio.run(main())
