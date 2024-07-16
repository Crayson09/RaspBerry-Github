

import discord
from discord import ui, app_commands
from discord.app_commands import Choice
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), status=discord.Status.online)

bot.run("")
