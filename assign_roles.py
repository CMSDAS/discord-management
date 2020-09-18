from asyncio.tasks import sleep
import os
import sys
from dotenv import load_dotenv
import discord
import gspread
from longex import ex_short
load_dotenv()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        server = client.guilds[0]

        for participant in participants:
            if not participant.id:
                print(f"{participant} has no Discord ID. Skipping.")
                continue
            role = discord.utils.find(lambda r: r.name == participant.ex, server.roles)
            if role:
                print(f"Role found: {participant.ex}")
                member = discord.utils.find(lambda m: m.name == participant.id, server.members)
                if member:
                    print(f"Member found: {participant.name}")
                    try:
                        await member.add_roles(role)
                    except Exception as e:
                        print(e)
                else:
                    print(f"Member not found: {participant.name}")
            else:
                print(f"Role {participant.ex} not found!")
            await sleep(1)
        sys.exit()


class Participant:
    def __init__(self, name='', id='', ex=''):
        self.name = name
        self.id = id
        self.ex = ex_short[ex]

    def __repr__(self):
        return f"{self.name} ({self.id}): {self.ex}"

gc = gspread.oauth()

g_sheet = gc.open_by_key("1u2E9clOiB7SBTmKiRTi_0iZfNi3AbxZwaTaOSsh9r9c")

# Sheet1:
#   Column 1: Name
#   Column 2: Discord
#   Column 3: Exercise

g_worksheet1 = g_sheet.get_worksheet(0)
g_names_1 = g_worksheet1.col_values(1)[1:]
g_ids = g_worksheet1.col_values(2)[1:]
g_exercises = g_worksheet1.col_values(3)[1:]

participants = []
for name_, id_, ex_ in zip(g_names_1, g_ids, g_exercises):
    participant = Participant(name=name_, id=id_, ex=ex_)
    participants.append(participant)

print(participants)


client = MyClient()
client.run(os.getenv("DISCORD_TOKEN"))