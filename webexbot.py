import os
import json
import discord
from discord.ext import commands


DS_TOKEN = "OTAwMDQzNjczNDIzNzIwNTU5.YW7k_Q.Gc226SwrlWIaTo2gweKVLQtYuGw"      # accesso al bot tramite token
DS_CMD = "vl!"                                                                # comando di attivazione del bot

# legge le informazioni sulle lezioni
with open("link.json") as f:
    lista_lezioni = json.load(f)

# instaurazione della connessione con discord
client = discord.Client()

# evento: messaggio di attivazione del bot
@client.event
async def on_ready():
    print(f'{client.user} è attivo')

# comando: invia il link della lezione con la richiesta
@client.command(aliases=[DS_CMD])
async def _vl(ctx, *, command):

# avvio del bot e running loop
client.run(DS_TOKEN)