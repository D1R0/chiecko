class convertor(msg):
        if msg.startswith("lei/euro:") or msg.startswith("euro/lei:"):
            if msg.startswith("lei/euro:"):
                content=float(msg.replace("lei/euro:",""))
                await bot.send_message(message.author,str(round(content/default,1))+" €")
            else:
                content=float(msgt.replace("euro/lei:",""))
                await bot.send_message(message.author,str(round(default*content,1))+" Lei")