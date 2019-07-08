import asyncio
import websockets
import os

async def response(websocket, path):
	message = await websocket.recv()
	print(f"We got the message from the client: {message}")
	await websocket.send("I can confirm I got your message!")
port = os.environ['PORT'] || 3000
start_server = websockets.serve(response, '', port=port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
