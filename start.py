#
#           YesBot start.py | Copyright (c) 2020 Mrmagicpie
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
import discord
import asyncio
from discord.ext import commands
import os
from config import TOKEN
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
async def get_prefix(bot, message):
    prefixes = ["yes/", "yes "]
    return commands.when_mentioned_or(*prefixes)(bot, message)
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
bot = commands.Bot(command_prefix=get_prefix, intents=discord.Intents.all())
bot.remove_command('help')
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
for cog in os.listdir('bot'):
    if cog.endswith('.py'):
        bot.load_extension(f"bot.{cog[:-3]}")
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
@bot.event
async def on_ready():

    print(f'''
|--------------------|
| Bot ready!         |
| Signed in as:      |
|    {bot.user}    |
|--------------------|
    ''')

    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Activity(name="Still waking up 😒",
                                                        type=discord.ActivityType.watching))

    await asyncio.sleep(10)
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name="dpy vs djs", type=5))

#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
bot.run(TOKEN)
