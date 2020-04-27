import asyncio
import sys

import boto3
import discord
from discord.ext import commands


class Bot(commands.bot.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_cog(AwsCog)

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


class AwsCog(commands.Cog)
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def startserver(self, ctx):
        print(f"Recieved command startserver from user {ctx.message.author}")
        ec2 = boto3.client("ec2")
        print("Starting ec2 instance")
        response = ec2.start_instances(
            InstanceIds=[
                'i-0986e940a442f36c0',
            ]
        )
        print(
            "Current state of instance: "
            f"{response['StartingInstances'][0]['CurrentState']['Name']}"
        )


if __name__ == '__main__':
    bot = Bot(command_prefix="!")
    bot.run(sys.argv[1])
