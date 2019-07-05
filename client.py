import asyncio
import websockets
import os
import webbrowser


async def message():
    port = int(os.environ['PORT'])
    webbrowser.open_new("webclient.html")
    async with websockets.connect(f"wss://abhi122.herokuapp.com:{port}") as socket:
        msg = "Hello!!"
        await socket.send(msg)
        print(await socket.recv())
        await socket.send("Good Bye!!")

asyncio.get_event_loop().run_until_complete(message())
asyncio.get_event_loop().run_forever()
