import os
import json
from datetime import datetime, time
from discord.ext import commands


DS_TOKEN = "OTAwMDQzNjczNDIzNzIwNTU5.YW7k_Q.Gc226SwrlWIaTo2gweKVLQtYuGw"      # accesso al bot tramite token        brock = OTAwMDQzNjczNDIzNzIwNTU5.YW7k_Q.Gc226SwrlWIaTo2gweKVLQtYuGw
DS_CMD = "^"                                                                  # comando di attivazione del bot      lory = OTAwMTYwNTY1NDc1OTU4ODI1.YW9R2g.I3-j3Xu8JddxiBAYoQ4KNLoqp1M


# restituisce il giorno e l'ora corrente
def retrieve_datetime():
    # data e ora corrente
    now = datetime.now()

    # ora corrente e giorno della settimana
    current_datetime = {
        "time":now.time(),
        "dotw":now.date().weekday()
    }

    return current_datetime
    


# legge le informazioni sulle lezioni
with open("link.json") as f:
    lista_lezioni = json.load(f)

# instaurazione della connessione con discord
client = commands.Bot(command_prefix=DS_CMD)

# evento: messaggio di attivazione del bot
@client.event
async def on_ready():
    print(f'{client.user} è attivo')

# comando: invia il link della lezione con la richiesta
@client.command(aliases=["vl"])
async def _vl(ctx):
    await ctx.send(f'ciao')

# comando: invia la data e l'ora                                        da sistemare - brock spiegami come si fa che non ho capito tanto bene i dict anche se mi sa che sono stra easy
@client.command(aliases=["data"])
async def _data(ctx):
    await ctx.send(retrieve_datetime())

# avvio del bot e running loop
client.run(DS_TOKEN)