# client.py

import asyncio
import websockets

async def receive_messages():
    uri = "ws://localhost:8000"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(receive_messages())
