import discord
import logging
from discord.client import _ColourFormatter
from discord.ext import commands
from discord.utils import get
from discord import app_commands
from time import sleep
from bot_utils import TOKEN, GUILD_ID

log = logging.getLogger("Disnight")
log.setLevel(logging.DEBUG)

stream = logging.StreamHandler()
stream.setFormatter(_ColourFormatter())
log.addHandler(stream)


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(
    command_prefix = "! ",
    help_command = None,
    intents = intents
)

@bot.event
async def on_ready():
    log.info("Disnight Ready!")
    await bot.tree.sync(guild=discord.Object(id=GUILD_ID))

@bot.tree.command(name="test",description="Test.",guild=discord.Object(id=GUILD_ID))
async def test(ctx):
    await ctx.send("Ça marche comme ça les slash commands ?")

bot.run(TOKEN)
