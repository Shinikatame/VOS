from discord import Client, Embed
from discord.ext.commands import Cog

from Components.Views.Registry import Registry

class Ready(Cog):
    def __init__(self, bot: Client):
        self.bot = bot

    @Cog.listener('on_ready')
    async def ready(self):
        print(f'{self.bot.user} logado')

        # guild = await self.bot.fetch_guild(942103135659388958)
        # channel = await guild.fetch_channel(963879101142302770)

        # role = guild.get_role(963918497526718535)
        # await channel.send(role.mention)

        # embed = Embed(color = 65280)
        # embed.title = 'Bem vindo a Team VØS - Vila Oculta do Sal.'
        # embed.description = 'Faça o registro para sabermos quem é você.'
        # embed.set_thumbnail(url = self.bot.user.avatar)

        # view = Registry()

        # await channel.send(embed = embed, view = view)


def setup(bot):
    bot.add_cog(Ready(bot))
