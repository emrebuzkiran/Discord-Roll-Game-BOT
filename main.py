import discord
from utils import *
from discord.ext import commands
import random
import asyncio
import time


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$roll'):
            await message.channel.send('The dice are rolling...... Guess the right number.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 6)

            time.sleep(5)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=7.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sorry, you took too long it was {answer}.')

            if int(guess.content) == answer:
                await message.channel.send(f'You are right {message.author.name}')
            else:
                await message.channel.send(f'Oops. It is actually {answer}.')


client = MyClient()

client.run(token)
