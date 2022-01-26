from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import discord
from discord.ext import commands
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from pyowm.weatherapi25 import observation

token = input('Enter your token: ')
##token = "ODk2MDU3MjkyNjYxODc4ODc0.YWBkYg.y-D0ZJMQbPaoUsuSywNSW6F5L1o"

bot = commands.Bot(command_prefix='!')

ban_words = ['qwe', 'asd', 'arsehole', 'balls', 'bitch', 'bollocks', 'bullshit', 'feck', 'pissed',
            'shit', 'cock', 'dick', 'dickhead', 'pussy', 'beaver', 'cunt', 'fuck', 'motherfucker']

@bot.event
async def on_ready():
    print('Bot was connected')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    msg = message.content.lower()
    for i in ban_words:
        if i in msg:
            await message.delete()
            await message.author.send(f'{message.author.name}, DONT WRITE IT ANYMORE!!!')

@bot.command(pass_context= True)
async def weather(ctx, arg):
    owm = OWM('b7ca9e58889c65158dfe9994fce5f839')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(str(arg))
    w = observation.weather

    temp1 = w.temperature('celsius')

    answer1 = ("In the", arg, w.detailed_status, "now")
    correcting = {'In the': 'In the', arg: arg, w.detailed_status: w.detailed_status, 'now': 'now', '"': '', ',': ''}
    final_correcting1 = []
    final_correcting2 = []
    for i in answer1:
        taking_key1 = correcting.get(i)
        final_correcting1.append(taking_key1)
    final_answer1 = " ".join(final_correcting1)
    await ctx.send(final_answer1)

    middle_temp = temp1.get('temp')
    answer2 = ("And", float(middle_temp), "in average")
    correcting2 = {'And': 'And', float(middle_temp): str(middle_temp), 'in average': 'in average', '"': '', ',': ''}
    for i in answer2:
        taking_key2 = correcting2.get(i)
        final_correcting2.append(taking_key2)
    final_answer2 = " ".join(final_correcting2)
    await ctx.send(final_answer2)


@bot.command(pass_context= True)
async def retry(ctx, arg):
    await ctx.channel.purge(limit = 1)
    await ctx.send(arg)

@bot.command(pass_context= True)
async def Help(message):
    await message.author.send(f'{message.author.name}, all comands:!retry, !ping, !good, !weather (City where you dont know weather), !clear (how many messages you want delete), also i delete not good words')
@bot.command(pass_context= True)
async def ping(ctx):
    author = ctx.message.author
    await ctx.send(f'{author.mention} pong')
@bot.command(pass_context= True)
async def good(ctx):
    author = ctx.message.author
    await ctx.send(f'{author.mention} Thanks')
@bot.command (pass_comtext = True)
async def clear(ctx, amount = 1):
    await ctx.channel.purge(limit = amount + 1)


bot.run(token)