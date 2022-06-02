#!/usr/bin/env python

"""echo server from https://websockets.readthedocs.io/en/stable/

to test  server run build-in client with

```console
$python -m websockets ws://localhost:8765/
Connected to ws://localhost:8765/.
> Hello world!
< Hello world!
Connection closed: 1000 (OK).
```

"""

import asyncio
import websockets

async def echo(websocket, path):
	async for message in websocket:
		await websocket.send(message)

async def main():
	print('listenning on ws://localhost:8765 address')
	async with websockets.serve(echo, "localhost", 8765):
		await asyncio.Future()  # run forever

asyncio.run(main())
