import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", description="Ceci est un bot pour un tuto YouTube")

@bot.event
async def on_ready():
    print("Le bot a démarer !")
    
@bot.command()
async def exemple(ctx, user: discord.User):
    await ctx.message.delete()
    await ctx.send("Exemple reçu !")
    embed = discord.Embed(title="Exemple d'embed : ", description="Ceci est un exemple d'embed !", color=discord.Colour.blue())
    embed.set_thumbnail(url="https://images.emojiterra.com/google/noto-emoji/v2.034/512px/26a0.png")
    embed.add_field(name=" auteur de la commande : ", value=ctx.author.name+"#"+ctx.author.discriminator, inline=True)
    embed.add_field(name=" personne qui a étais désigner : ", value=user.name+"#"+user.discriminator, inline=False)
    await ctx.send(embed=embed)
    channel = bot.get_channel(967389841048354886)
    await channel.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, user: discord.User, *,reason=None):
    if reason is None:
        embed0 = discord.Embed(title=":warning: Erreur dans la commande de warn", description="L'argument `reason` est requis !",color=discord.Color.orange())
        await ctx.send(embed=embed0)
    else:
        await ctx.message.delete()
        embed = discord.Embed(title="Un utilisateur a reçu un warn", description="un modo a avertie un membre", color=discord.Color.blue())
        embed.set_thumbnail(url="https://images.emojiterra.com/google/noto-emoji/v2.034/512px/26a0.png")
        embed.add_field(name="Invockeur : ", value=ctx.author.name+"#"+ctx.author.discriminator)
        embed.add_field(name="Membre avertie : ", value=user.name+"#"+user.discriminator, inline=True)
        embed.add_field(name="Raison : ", value=reason, inline=False)
        await ctx.send(embed=embed)

bot.run("TOKEN")
