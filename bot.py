import asyncio
import sys

import boto3
import discord
from discord.ext import commands


class Bot(commands.bot.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
