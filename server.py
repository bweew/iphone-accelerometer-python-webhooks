#!/usr/bin/env python3
import asyncio
import websockets
import subprocess
import json

HOST = "0.0.0.0"
PORT = 8000

def play_sound(filename):
    subprocess.Popen(["play", "-q", filename])  # non-blocking playback

async def handler(ws):
    async for message in ws:
        try:
            print("Received:", repr(message))  # debug
            data = json.loads(message)
            btn = data.get("button", "").strip().lower()
            if btn == "up":
                play_sound("up.wav")
            elif btn == "down":
                play_sound("down.wav")
        except Exception as e:
            print("Error:", e)

async def main():
    async with websockets.serve(handler, HOST, PORT):
        print(f"WebSocket server running on ws://{HOST}:{PORT}")
        await asyncio.Future()  # run forever

asyncio.run(main())

