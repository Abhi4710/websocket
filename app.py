import asyncio
import websockets


async def response(websocket, path):
    message = await websocket.recv()  # receive the message
    print("Message Received!")
    print(f"Message: {message}")
    await websocket.send("Message receive successfully!!")  # send the message back
print("hello")
start_server = websockets.serve(response, 'localhost', 1234) ## (response, host, port)

asyncio.get_event_loop().run_until_complete(start_server)
print("Bye")
asyncio.get_event_loop().run_forever()

