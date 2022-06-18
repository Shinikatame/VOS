from discord import Client
from discord.ext.commands import Cog

from Components.Views.Registry import Registry as View

from Modules.Json import jsonLoad

ids = jsonLoad('Ids')

class Registry(Cog):
    def __init__(self, bot: Client):
        self.bot = bot

    @Cog.listener('on_ready')
    async def registry(self):
        view = View()
        self.bot.add_view(view)

def setup(bot):
    bot.add_cog(Registry(bot))