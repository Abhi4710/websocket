import asyncio
import websockets


async def message():
    port = int(os.environ['PORT'])
    async with websockets.connect(f"wss://abhi122.herokuapp.com:{port}") as socket:
        msg = input("what do you want to send?")
        await socket.send(msg)
        print(await socket.recv())

asyncio.get_event_loop().run_until_complete(message())
asyncio.get_event_loop().run_forever()
