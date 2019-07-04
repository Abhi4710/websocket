import asyncio
import websockets
import os


async def response(websocket, path):
    message = await websocket.recv()  # receive the message
    print("Message Received!")
    print(f"Message: {message}")
    await websocket.send("Message receive successfully!!")  # send the message back
print("hello")
print(os.environ['PORT'])
os.environ['PORT'] = 1234
port = int(os.environ['PORT'])
print(os.environ['PORT'])
start_server = websockets.serve(response, 'abhi122.herokuapp.com', port=port) ## (response, host, port)

asyncio.get_event_loop().run_until_complete(start_server)
print("server open")
asyncio.get_event_loop().run_forever()

