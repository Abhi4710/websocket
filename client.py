import asyncio
import websockets


async def message():
    async with websockets.connect("wss://abhi122.herokuapp.com:31793") as socket:
        msg = input("what do you want to send?")
        await socket.send(msg)
        print(await socket.recv())

asyncio.get_event_loop().run_until_complete(message())
asyncio.get_event_loop().run_forever()