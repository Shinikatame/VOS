from discord import Client, slash_command, Interaction
from discord.ext.commands import Cog

class Ping(Cog):
    def __init__(self, bot: Client):
        self.bot = bot

    @slash_command(description = 'Veja meu ping')
    async def ping(self, inter: Interaction):
        msg = f'{self.bot.latency*100:.2f}ms'
        await inter.response.send_message(msg, ephemeral = True)

def setup(bot):
    bot.add_cog(Ping(bot))
