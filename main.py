#is working yaaay

import discord
import os
import requests

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


def get_quote(possibelnumber):
  response_string = "http://numbersapi.com/" + str(possibelnumber)
  print(response_string)
  responses = requests.get(response_string)
  # print(responses.text)
  return responses.text


@client.event
async def on_ready():
  print()
  # print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

  if message.author == client.user:
    return

  msg = message.content
  # print(message)
  # print(message.content)
  possible_message = list(msg.split())
  for i in range(len(possible_message)):
    if possible_message[i].isnumeric():
      print(possible_message[i])
      quote = get_quote(possible_message[i])
      # print(quote)
      await message.channel.send(quote)
      break


client.run(os.getenv('TOKEN', ''))
