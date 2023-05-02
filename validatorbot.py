import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load the bot token from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up the bot with the desired command prefix
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Define the 'ask' command to handle questions
@bot.command(name='ask', help='Ask a question about validators and nodes in the web3 ecosystem.')
async def ask(ctx, *, question):
    response = get_response(question)
    await ctx.send(response)

def get_response(question):
    # TODO: Replace this function with your ChatGPT integration
    # and any necessary API calls to provide accurate and up-to-date information.
    response = f"I received your question: {question}\nReplace this with a proper response using ChatGPT and relevant APIs."
    return response

bot.run(TOKEN)
