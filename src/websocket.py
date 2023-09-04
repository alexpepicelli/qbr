import asyncio
import websockets
import threading

import helpers
import marker_outlet
import gaze_outlet


# colors = []

# def update_colors(col):
#     global colors
#     colors = col
#     print("test", colors)


def main():
    # create handler for each connection
    async def handler(websocket):
        async for msg in websocket:
            reply = f"Data received, nothing to reply:  {msg}!"
            colors = helpers.get_color_snapshot()
            if msg == "GET":
                if len(colors) > 0:
                    # await asyncio.sleep(0.5)
                    colors = helpers.get_color_snapshot()
                    reply = "GET:" + ','.join(colors)
                    print("GET REPLY:", reply)
            if msg == "SUCCESS":
                helpers.set_color_snapshot([])
            if "MARKER" in msg:
                if "GAZE" in msg:
                    gaze_outlet.push(msg[7:])
                else:
                    marker_outlet.push(msg[7:])
            await websocket.send(reply)
            await asyncio.sleep(0)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    server = websockets.serve(handler, "10.220.54.222", 5564)
    loop.run_until_complete(server)
    loop.run_forever()


ws = threading.Thread(target=main, daemon=True).start()
