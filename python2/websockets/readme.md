# WebSocket samples

install websocket library with

```bash
sudo pip3 install websockets
```

command


`ws_client.html`: Web WebSocket sample client, can be used with echo server implementation `echo.py`. 

Run `echo.py` with

```
./echo.py
```

command and open `ws_client.html` in a Web browser window.

> tested with firefox browser


## Secure WebSockets

`localhost.key/crt/pem`: self-signed localhost certificate

> describe commands used to generate certificate

`server_secure.py`: implements Secure WebSocket server from [Encrypt connections](https://websockets.readthedocs.io/en/stable/intro/quickstart.html#encrypt-connections) tutorial

`client_secure.py`: implements Secure WebSocket client from [Encrypt connections](https://websockets.readthedocs.io/en/stable/intro/quickstart.html#encrypt-connections) tutorial

`echo_secure.py`: WebSocket Secure (WSS) echo server implementation

Just run server with

```bash
./server_secure.py
```

command and then client with

```bash
./client_secure.py
```

command. After you enter name into the client console the server should reply with `Hello $NAME` this way

```console
$ ./client_secure.py 
What's your name? John
>>> John
<<< Hello John!
```

```console
$ ./server_secure.py 
<<< John
>>> Hello John!
```
