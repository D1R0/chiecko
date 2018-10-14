import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import platform
import datetime
from color import randomcolor
from pathlib import Path
#import requests as rq
#import simplejson as json
#from champs import champs
import os

token = str(os.eviron("BOT_TOKEN")

#api=str(os.eviron.get("RIOT_TOKEN"))



client = commands.Bot(command_prefix='')
citire= open("prefix.txt","r")
pr=citire.read()
citire.close()
base="data/"
default=4.66

rgb = ("0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F")

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

    return await bot.change_presence(game=discord.Game(name="for help, type "+pr))

#@bot.command(pass_context=True)
#async def ping(cnt):
#    await bot.say("Pong!")

@bot.event
async def on_message(message):
    #print(str(message.author)+":"+message.content)

    if message.content == "prefix":
        await bot.send_message(message.channel,pr)
    
    if message.content.startswith("Set prefix:"):
        if message.author.id == "336810396340060161":
            msg=message.content.replace("Set prefix:","")
            with open("prefix.txt","w") as file:
                file.write(msg)
            await bot.send_message(message.channel,"Change!")

        else:
            await bot.send_message(message.channel,"Missing permission!")

    if message.content == pr:
        if message.author.id != "479310380058017792":
            embed = discord.Embed(title="", description="", colour=0x01DFD7)
            embed.add_field(name=":owl:", value="**PreAlpha** `0.1.0`", inline=True)
            embed.add_field(name="For help", value=pr+"help", inline=True)
            embed.add_field(name="*By* **D1r0#6706**", value=":copyright: 2018", inline=False)       
            embed.set_thumbnail(url=bot.user.avatar_url)
            await bot.send_message(message.channel, embed=embed)

    if message.content.startswith(pr+"banner:"):
        msg=str(message.content.replace(">banner:","",1))
        emb = discord.Embed(title="Banner", description="`by %s`"%(message.author), colour=0x00aeff)
        emb.set_image(url='https://dummyimage.com/1920x1080/%s/%s&text=%s'%(randomcolor(rgb),randomcolor(rgb),msg))
        await bot.send_message(message.channel, embed=emb)

    if message.content == pr+"help":
        embed = discord.Embed(title="Description", description="Commands", colour=0x01DFD7)
        embed.add_field(name="**Register in Base Data:dividers:**", value=pr+"reg", inline=True)
        embed.add_field(name="**View stats:iphone:**", value="'status'", inline=True)
        embed.add_field(name="**Set stats:moneybag:**", value="'set:[Value]'", inline=True)
        embed.add_field(name="**Create a field:bar_chart:**", value="'addfield:[Name]'", inline=True)
        embed.add_field(name="**Remove a field:bar_chart:**", value="'delfield:[Name]'", inline=True)   
        embed.add_field(name="**Gathering or decreasing:money_with_wings:**", value="'add:[The position of the field]/[Value]'", inline=True)              
        embed.add_field(name="**Convert money:gem:**", value="'lei/euro:[Value]' or 'eruo/lei:[Value]'", inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await bot.send_message(message.channel, embed=embed)

    if message.content ==pr+"reg":
        name=str(message.author.id)
        sufix=".txt"
        valid=True
        file=Path(base+name+sufix)
        if file.is_file():
            await bot.send_message(message.channel,"u are reg")
        else:
            valid=False
        if valid==False:
            file=open(base+name+sufix,"w")
            file.write("Slot:0 ")
            file.close()
            await bot.send_message(message.channel, "Succes")
            await bot.send_message(message.author, "A here 4 u")        
            embed = discord.Embed(title="", description="", colour=0x01DFD7)
            embed.add_field(name=":owl:", value="**PreAlpha** `0.1.0`", inline=False)     
            embed.add_field(name="*", value="*I'm here fot you!* `0.1.0`", inline=False)
            embed.add_field(name="*By* **D1r0#6706**", value=":copyright: 2018", inline=False)       
            embed.set_thumbnail(url=bot.user.avatar_url)
            await bot.send_message(message.author, embed=embed)

    if message.content.startswith("set:"):
        dinamic=message.author.id
        id=str(message.author.id)+"txt"
        file=base+str(message.author.id)+".txt"
        if Path(file).is_file():
            slot=message.content.replace("set:","")
            data=open(file,"r+")
            sloti=data.read()
            data.close()
            word=sloti
            word=sloti.split()[0]
            sloti=sloti.replace(word.split(":")[1],slot,1)
            data=open(file,"r+")
            data.write(sloti)
            data.close()
            await bot.send_message(message.author,"Successful!")
        else:
            await bot.send_message(message.author,"Pls reg")

    if message.content=="status" or message.content=="Status" :
        dinamic=message.author.id
        id=str(message.author.id)+"txt"
        file=base+str(message.author.id)+".txt"
        if Path(file).is_file():
            status=open(file,"r")
            await bot.send_message(message.author,"**"+status.read()+"**")
        else:
            await bot.send_message(message.author,"Pls reg")            

    if message.content.startswith("add:"):
        conent=message.content.replace("add:","",1)
        position=int(conent.split("/")[0])
        suma=float(conent.split("/")[1])
        dinamic=message.author.id
        id=str(message.author.id)+"txt"
        file=base+str(message.author.id)+".txt"
        if Path(file).is_file():
            data=open(file,"r+")
            sloti=data.read()
            data.close()
            word=sloti
            word=sloti.split()[position]
            if float(word.split(":")[1])>=0:
                suma=float(word.split(":")[1])+suma
                final=word.split(":")[0]+":"+str(round(suma,1))
                sloti=sloti.replace(word,final,1)
                data=open(file,"r+")
                data.write(sloti)
                data.close()
                await bot.send_message(message.author,str(suma)+"** in field **"+word.split(":")[0]+"**") 
            else:
                await bot.send_message(message.author,"Not found!")   
        else:
            await bot.send_message(message.author,"Pls reg")

    if message.content.startswith('delfield:'):
        position=int(message.content.replace("delfield:",""))
        dinamic=message.author.id
        id=str(message.author.id)+"txt"
        file=base+str(message.author.id)+".txt"
        if position>0:
            if Path(file).is_file():
                data=open(file,"r+")
                content=data.read()
                data.close()
                word=str(content.split()[position])+" "
                sloti=content.replace(word,"") 
                data=open(file,"w+")
                data.write(sloti)
                data.close()
                await bot.send_message(message.author,"Removed Field "+"**"+word.split(":")[0]+"**") 
            else:
                await bot.send_message(message.author,"Pls reg") 
        else:
            await bot.send_message(message.author,"Can not access that position!")  
                
    if message.content.startswith("addfield:") or message.content.startswith("Addfield:"):
        filed=message.content.replace("addfield:","")+":0 "
        dinamic=message.author.id
        id=str(message.author.id)+"txt"
        file=base+str(message.author.id)+".txt"
        if Path(file).is_file():
            data=open(file,"a+")
            data.write(filed)
            data.close()
            await bot.send_message(message.author,"Added Field "+"**"+filed.split(":")[0]+"**")
        else:
            await bot.send_message(message.author,"Pls reg")

    if message.content.startswith("lei/euro:") or message.content.startswith("euro/lei:"):
        if message.content.startswith("lei/euro:"):
            content=float(message.content.replace("lei/euro:",""))
            await bot.send_message(message.author,str(round(content/default,1))+" €")
        else:
            content=float(message.content.replace("euro/lei:",""))
            await bot.send_message(message.author,str(round(default*content,1))+" Lei")

bot.run(token)
