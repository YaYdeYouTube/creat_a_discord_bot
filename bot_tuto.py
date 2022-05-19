from turtle import title
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", description="Ceci est un bot pour un tuto YouTube")

@bot.event
async def on_ready():
    channel = bot.get_channel("ID de salon")
    await channel.send("Mesage")

bot.run("OTc2NTM3NzU1NzMzNTk4MjQ5.GJ_FyD.d4gTWo0MC4ugzcguya1DiNC_heeWrfaDHwLFJk")