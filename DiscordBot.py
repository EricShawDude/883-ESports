import discord
import random
import os
from discord import app_commands
from discord.ext import commands, tasks
from discord.utils import get
from datetime import datetime
from dotenv import load_dotenv

load_dotenv() # Loads the environment variables from the .env file, which is where the bot token is stored. This allows the bot to access the token securely without hardcoding it into the code.

description = ""

class User:
    def __init__(self, first_name: str, last_name: str, 
                discord_user: str, discord_id: int, 
                rank: str, roles: list, unit: int, team_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.discord_user = discord_user
        self.discord_id = discord_id
        self.rank = rank
        self.roles = roles
        self.unit = unit
        self.team_name = team_name


# implement hashmap for users 
# implement a function to check if a user is in the hashmap and assign roles accordingly

intents = discord.Intents.all()
client = discord.Client(intents=intents) #Declares the bot client and sets the intents to all, which allows the bot to access all events and data from the server. This is necessary for the bot to function properly and assign roles, check user information, etc.
bot = commands.Bot(command_prefix="/", description=description, intents=intents) 
tree = app_commands.CommandTree(client) # Command tree
dateStr = datetime.today().strftime('%Y-%m-%d')
day = int(datetime.today().day) 

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="883 E-Sports Tournament"))
    await tree.sync(guild=discord.Object(id=1334394629746851913))
    channel = client.get_channel(1349470222532345989)

    await channel.send(f"Bot is online and running on {dateStr}")

@tree.command(
    name = "join",
    description= "Sign-in for the tournament and get assigned roles.",
    guild = discord.Object(id=1334394629746851913)
)
async def join(interaction: discord.Interaction):
    guild = await client.fetch_guild(1334394629746851913)
    member = await guild.fetch_member(interaction.user.id)

    val = guild.get_role(1334397946720157727)

    gameIds = {
                "Valorant": val,

    }

try:
    client.run(os.getenv('token')) # This command gets the token from the .env file and runs the bot
except Exception as e:
    print("debug")
    print(e)
    print(e.args)

