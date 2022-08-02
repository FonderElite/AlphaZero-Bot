import discord,os,json,random
from discord.ext import commands

count = 0
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    channels = [1003260639915016202,995671347877384192]
    activity = discord.Game(name="Neural Networks")
    await bot.change_presence(activity=activity)
    bot_channel = bot.get_channel(channels[0])
    await bot_channel.send('Up')

@bot.event
async def on_message(message):
    if message.author.id == 1003789205178167317:
        return
    users = []
    messages = []
    users.append(message.author)
    messages.append(message.content)
    emoji = ['🤬','🤯','🥵','👻','💀','👽']
    word_present = True if message.content in open("messages.txt","r").read().split() else False
    if word_present == False:
        with open("messages.txt","a") as openf:
            append_f = openf.write(f"{message.content}\n") 
    with open("messages.txt","r") as readf:
        read_file = readf.read().splitlines()
        random_word = random.choice(read_file)
        await message.reply(random_word)
    for i in emoji:
        await message.add_reaction(i)
    

bot.run("MTAwMzc4OTIwNTE3ODE2NzMxNw.GBE-0z.d0rCl1gsIYsKfvY84M3zfZ-k5SEJPxXmU3zyQ4")

