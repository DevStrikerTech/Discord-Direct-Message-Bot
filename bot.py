import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=commands.when_mentioned_or("^"), case_insensitive=True)
client.remove_command("help")


def check_team(ctx):
    return client.get_guild('ID REQUIRED HERE').get_role('ID REQUIRED HERE') in ctx.author.roles


@client.event
async def on_connect():
    print("MODBOX STARTED")


@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    if message.author != message.author.bot:
        if not message.guild:
            await client.get_guild('ID REQUIRED HERE').get_channel('ID REQUIRED HERE').send(
                f"User Mention: {message.author.mention}\nUsername: {message.author}\nUser-ID: {message.author.id}\n\nMessage:\n{message.content}")
    await client.process_commands(message)


@client.command()
@commands.check(check_team)
async def dm(ctx, member: discord.Member, *, text):
    await member.send(text)

@client.event
async def on_resumed():
    print("MODBOX RECONNECTED")


client.run('TOKEN HERE', reconnect=True)
