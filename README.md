# Gifts-Counter

At first the library that this works from is From https://github.com/isaackogan/TikTokLive

This Program is Simple but to understand how it works you have to visit the site and understand the Library that is it brought from.

# Define a global variable to store the total number of coins
total_coins = 0

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="(insert your desired username from where you want to web scrape)") for example @xxxlily04. remove the bracket().
# For Example
client: TikTokLiveClient = TikTokLiveClient(unique_id="@xxxlily04")

# Define how you want to handle specific events via decorator. This Code connects to The Live.
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)
# Counts the Gift that has been Given to the user mentioned above in coins.
@client.on("gift")
async def on_gift(event: GiftEvent):
    global total_coins
    total_coins += 1
    print(f"Gift: {event.gift.id} was given, total coins: {total_coins}")
# Runs the command
def run_client():
    client.run()


thread = threading.Thread(target=run_client)
thread.start()

while True:
    pass

Enjoy the Web Scrapping
