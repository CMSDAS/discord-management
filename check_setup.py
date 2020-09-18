import os
import discord
from dotenv import load_dotenv
load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print(self.users)
        print(self.guilds)
        server = client.guilds[0]
        member = discord.utils.find(lambda m: m.nick == 'Clemens Lange', server.members)
        print(member)

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(os.getenv("DISCORD_TOKEN"))