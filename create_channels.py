from asyncio.tasks import sleep
import os
import sys
import discord
from dotenv import load_dotenv
from longex import ex_short
load_dotenv()

N_VOICE = 5
N_TEXT = 5

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        server = client.guilds[0]
        print(ex_short)
        for ex in ex_short.items():
            role = discord.utils.find(lambda r: r.name == ex[1], server.roles)
            if role:
                print("Role exists already - deleting")
                try:
                    await role.delete()
                except Exception as e:
                    print(e)
                    sys.exit()
            f_role = discord.utils.find(lambda r: r.name == f"{ex[1]}-facil", server.roles)
            if f_role:
                print("Facilitator role exists already - deleting")
                try:
                    await f_role.delete()
                except Exception as e:
                    print(e)
                    sys.exit()
            category = discord.utils.find(lambda c: c.name == ex[1], server.categories)
            if category:
                print("Category exists already - deleting")
                for v_channel in category.voice_channels:
                    try:
                        await v_channel.delete()
                    except Exception as e:
                        print(e)
                for channel in category.text_channels:
                    try:
                        await channel.delete()
                    except Exception as e:
                        print(e)
                try:
                    await category.delete()
                except Exception as e:
                    print(e)
                    sys.exit()

            print(f"Creating role for {ex}")
            try:
                role = await server.create_role(name=ex[1], mentionable=True)
                print(role)
            except Exception as e:
                print(e)
                sys.exit()
            print(f"Creating facilitator role for {ex}")
            try:
                f_role = await server.create_role(name=f'{ex[1]}-facil', mentionable=True)
                print(f_role)
            except Exception as e:
                print(e)
                sys.exit()
            print(f"Creating category for {ex}")
            overwrites = {
              server.default_role: discord.PermissionOverwrite(read_messages=False),
              role: discord.PermissionOverwrite(read_messages=True),
              f_role: discord.PermissionOverwrite(read_messages=True, manage_messages=True, mute_members=True, priority_speaker=True, move_members=True)
            }
            try:
                category = await server.create_category(ex[1], overwrites=overwrites, position=3)
            except Exception as e:
                print(e)
                sys.exit()
            print(category)
            for i in range(N_VOICE):
                try:
                    v_channel = await server.create_voice_channel(f"{ex[1]} voice {i}", category=category)
                except Exception as e:
                    print(e)
                    sys.exit()
                print(v_channel)
            for i in range(N_TEXT):
                try:
                    t_channel = await server.create_text_channel(f"{ex[1]}-{i}", category=category)
                except Exception as e:
                    print(e)
                    sys.exit()
                print(t_channel)
            await sleep(5)

        sys.exit()

client = MyClient()
client.run(os.getenv("DISCORD_TOKEN"))