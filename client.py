import asyncio
import websockets
import os
import codecs


async def message():
    port = int(os.environ['PORT'])
    f = codecs.open("webclient.html", 'r', 'utf-8')
    async with websockets.connect(f"wss://abhi122.herokuapp.com:{port}") as socket:
        msg = "Hello!!"
        await socket.send(msg)
        print(await socket.recv())
        await socket.send("Good Bye!!")

asyncio.get_event_loop().run_until_complete(message())
asyncio.get_event_loop().run_forever()
