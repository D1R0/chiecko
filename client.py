import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import platform
import os


bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__,platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(bot.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(bot.user.id))
    print('Ready')
    print('--------')
    print('Credits D1R0')

    return await bot.change_presence(game=discord.Game(name="Cava"))

@bot.event
async def on_member_join(member):
    channel = member.server.get_channel("539153400588402698")
    fmt = '{0.mention}, bun venit in **{1.name}.**:tada:  Esti **al {2}-lea Membru!**:gem:'
    await bot.send_message(channel, fmt.format(member, member.server, str(len(set(bot.get_all_members())))))
    role=discord.utils.get(member.server.roles,id="430467236633772043")
    await bot.add_roles(member,role)

@bot.event
async def on_member_remove(member):
    channel = member.server.get_channel("539119138463809539")
    fmt = '**{0.name}** tocmai a parasit **{1.name}**. See you again!'
    await bot.send_message(channel, fmt.format(member, member.server))
 
@bot.event
async def on_message(message):
    id=message.author.id
    channel=message.channel
    content=message.content
    if content == "servers":
        if id == '336810396340060161':
            await bot.wait_until_ready()
            while not bot.is_closed:
                for server in bot.servers:
                    await bot.send_message(message.channel,server.id+" "+server.name)
                await asyncio.sleep(600)

    
bot.run(str(os.environ.get("BOT_TOKEN")))
