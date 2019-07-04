import asyncio
import websockets

async def response(websocket, path):
    message = await websocket.recv()  # receive the message
    print("Message Received!")
    print(f"Message: {message}")
    await websocket.send("Message receive successfully!!")  # send the message back

start_server = websockets.serve(response, '', 1234) ## (response, host, port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
