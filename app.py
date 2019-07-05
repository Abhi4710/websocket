import asyncio
import websockets
import os


async def response(websocket, path):
    message = await websocket.recv()  # receive the message
    print("Message Received!")
    print(f"Message: {message}")
    await websocket.send("Message receive successfully!!")  # send the message back
print("hello")
print(os.environ)
# port = int(os.environ)
start_server = websockets.serve(response, '', port=65432) ## (response, host, port)

asyncio.get_event_loop().run_until_complete(start_server)
print("server open")
asyncio.get_event_loop().run_forever()

