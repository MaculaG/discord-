import discord
from discord.ext import commands
from groq import Groq

client = Groq(api_key="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")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

messages = []

@bot.event
async def on_message(message):
    global messages
    if message.author == bot.user:
        return
    if not message.mentions or bot.user not in message.mentions:
        return
    messages.append({"role": "user", "content": message.content})
    if len(messages) > 6:
        messages = messages[-6:]
    response = client.chat.completions.create(model='llama3-70b-8192', messages=messages, temperature=0)
    response_content = response.choices[0].message.content
    if len(response_content) > 2000:
        response_content = response_content[:1997] + '...'
    await message.channel.send(response_content)
    messages.append({"role": "assistant", "content": response_content})

bot.run("MTIxNjgwOTgzNTYyMzA4ODI4OA.GzyIQy.U7udS6Ho2RnQZHH4jFNOqkY4ZrwgaMX_E-tmJo")
