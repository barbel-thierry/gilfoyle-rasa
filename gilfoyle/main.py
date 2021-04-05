import logging
import os
import sys

import discord
from dotenv import load_dotenv

from gilfoyle import scapegoat, random_values, game, score, quote

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if scapegoat.check(message):
        log_for('scapegoat', message)
        await message.channel.send(scapegoat.pick())
    elif random_values.check(message):
        log_for('random_values', message)
        await message.channel.send(random_values.global_result())
    elif game.check(message):
        log_for('game', message)
        await message.channel.send(game.play(message))
    elif score.check(message):
        log_for('score', message)
        await message.channel.send(score.display())
    else:
        log_for('quote', message)
        await message.channel.send(quote.response(message))


def log_for(reagent, message):
    logging.info('[%s][%s] %s', message.author, reagent, message.content)


if __name__ == '__main__':
    client.run(TOKEN)
