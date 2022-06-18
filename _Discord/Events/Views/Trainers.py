from discord import Client
from discord.ext.commands import Cog

from Components.Views.Trainer.Standard import Standard

from DataBase.Trainers import find

from Modules.Json import jsonLoad

ids = jsonLoad('Ids')

class Trainers(Cog):
    def __init__(self, bot: Client):
        self.bot = bot

    @Cog.listener('on_ready')
    async def trainers(self):
        data = find()

        guild = self.bot.get_guild(ids['guild'])
        channel = guild.get_channel(ids['trainers'])

        for payload in data:
            message = await channel.fetch_message(payload['message'])
            view = Standard(self.bot, payload)

            if message.components[0].to_dict() != view.to_components()[0]:
                await message.edit(view = view)

            else:
                self.bot.add_view(view, message_id = payload['message'])

def setup(bot):
    bot.add_cog(Trainers(bot))