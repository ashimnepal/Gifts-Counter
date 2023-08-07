
import threading

from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import GiftEvent, ConnectEvent

# Define a global variable to store the total number of coins
total_coins = 0

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@xxxlily04")


# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)

@client.on("gift")
async def on_gift(event: GiftEvent):
    global total_coins
    total_coins += 1
    print(f"Gift: {event.gift.id} was given, total coins: {total_coins}")


def run_client():
    client.run()


thread = threading.Thread(target=run_client)
thread.start()

while True:
    pass
