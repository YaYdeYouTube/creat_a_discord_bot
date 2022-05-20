import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", description="bot description")

@bot.event
async def on_ready():
    print("Le bot a démarer !")
    

@bot.command()
async def exemple(ctx):
    # await ctx.message.delete()
    # await ctx.send("Ceci est un message exemple !")
    embed=discord.Embed(title="Exemple d'Embed !", description="Exemple 1", color=discord.Color.blue())
    embed.set_thumbnail(url="https://e7.pngegg.com/pngimages/794/464/png-clipart-line-black-special-olympics-area-m-example-stamp-icon-cdr-text.png")
    embed.add_field(name="Exemple 2", value="Voici un dexième exemple !")
    embed.add_field(name="Exemple 3", value="Ceci est un troisième exemple !", inline=True)
    embed.add_field(name="Exemple 4", value="Ceci est un quatrième exemple !", inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, user: discord.User, *,reason=None):
    if reason is None:
        await ctx.message.delete()
        embed0 = discord.Embed(title="Erreur dans la commande de warn !", description="L'argument `reason` est requis !", color=discord.Color.blue())
        await ctx.send(embed=embed0)
    else:
        await ctx.message.delete()
        embed1 = discord.Embed(title="Un utilisateur a reçu un warn !", description="Un modo a avertie un membre", color=discord.Color.blue())
        embed1.set_thumbnail(url="https://images.emojiterra.com/google/noto-emoji/v2.034/512px/26a0.png")
        embed1.add_field(name="Membre avertie : ", value=user.name+"#"+user.discriminator)
        embed1.add_field(name="Invocker : ", value=ctx.author.name+"#"+ctx.author.discriminator, inline=True)
        embed1.add_field(name="Raison : ", value=reason, inline=False)
        await ctx.send(embed=embed1)

bot.run("BOT TOKEN")
