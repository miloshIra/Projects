import discord
import random

GREETING = ["Autobots ready to roll out!", "Ready, boss.", "All systems operational."]
CLIENT_TOKEN = "OTAzMzEwMzA3NjYzOTM3NTg2.YXrHSA.1qlwDAADaSBZS8BueFarf3dvdZY"
BOT_TOKEN = ""

client = discord.Client()


@client.event
async def on_ready():
    print(random.choice(GREETING))
    # message.channel.send(random.choice(GREETING))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    response = random.randint(1, 100)
    if response <= 5:
        await message.channel.send("Shut up, bitch..")


@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edited a message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}\n'
        "\n"
        "HAH! Gotta ya!"
    )


client.run(CLIENT_TOKEN)
