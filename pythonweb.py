import asyncio
import datetime
import random
import websockets
import os


async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)
        
port = int(os.environ['PORT']))
print(port)
start_server = websockets.serve(time, '', port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
