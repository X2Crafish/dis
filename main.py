import os
import discord # type: ignore
from discord.ext import commands # type: ignore
from discord import app_commands # type: ignore
from dotenv import load_dotenv

from myserver import server_on

load_dotenv()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


# //////////////////// Bot Event /////////////////////////
@bot.event
async def on_ready():
    print("Bot Online!")
    print("555")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1140633489520205934)
    text = f"Welcome to the server, {member.mention}!"

    emmbed = discord.Embed(
        title='Welcome to the server!',
        description=text,
        color=0x66FFFF
    )

    await channel.send(text)
    await channel.send(embed=emmbed)
    await member.send(text)


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1140633489520205934)
    text = f"{member.name} has left the server!"
    await channel.send(text)


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    mes = message.content
    if mes == 'hello':
        await message.channel.send("Hello It's me")
    elif mes == 'hi bot':
        await message.channel.send("Hello, " + str(message.author.name))

    await bot.process_commands(message)


# ///////////////////// Commands /////////////////////
@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.name}!")


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.tree.command(name='hellobot', description='Replies with Hello')
async def hellocommand(interaction):
    await interaction.response.send_message("Hello It's me BOT DISCORD")


@bot.tree.command(name='name', description='Ask your name')
@app_commands.describe(name="What's your name?")
async def namecommand(interaction, name: str):
    await interaction.response.send_message(f"Hello {name}")


@bot.tree.command(name='help', description='Bot Commands')
async def helpcommand(interaction):
    emmbed = discord.Embed(
        title='Help Me! - Bot Commands',
        description='Bot Commands',
        color=0x66FFFF,
        timestamp=discord.utils.utcnow()
    )

    emmbed.add_field(name='/hellobot', value='Hello Command', inline=True)
    emmbed.add_field(name='/name', value='Ask your name', inline=True)
    emmbed.add_field(name='/help', value='Help info', inline=False)

    emmbed.set_author(
        name='Author',
        url='https://www.youtube.com/@maoloop01/channels',
        icon_url='https://yt3.googleusercontent.com/0qFq3tGT6LVyfLtZc-WCXcV9YyEFQ0M9U5W8qDe36j2xBTN34CJ20dZYQHmBz6aXASmttHI=s900-c-k-c0x00ffffff-no-rj'
    )

    emmbed.set_thumbnail(
        url='https://yt3.googleusercontent.com/0qFq3tGT6LVyfLtZc-WCXcV9YyEFQ0M9U5W8qDe36j2xBTN34CJ20dZYQHmBz6aXASmttHI=s900-c-k-c0x00ffffff-no-rj'
    )

    emmbed.set_image(
        url='https://i.ytimg.com/vi/KZRa9DQzUpQ/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCfWDgiBYjFJtrUasd5yxmQZJG_cg'
    )

    emmbed.set_footer(
        text='Footer',
        icon_url='https://yt3.googleusercontent.com/0qFq3tGT6LVyfLtZc-WCXcV9YyEFQ0M9U5W8qDe36j2xBTN34CJ20dZYQHmBz6aXASmttHI=s900-c-k-c0x00ffffff-no-rj'
    )

    await interaction.response.send_message(embed=emmbed)


server_on()
bot.run(os.getenv('TOKEN'))
