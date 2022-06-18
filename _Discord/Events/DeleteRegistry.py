from discord import Client
from discord.ext.commands import Cog
from discord.raw_models import RawMessageDeleteEvent

from DataBase.Trainers import find, delete

from Modules.Json import jsonLoad

ids = jsonLoad('Ids')

class Delete(Cog):
    def __init__(self, bot: Client):
        self.bot = bot

    @Cog.listener('on_raw_message_delete')
    async def registry(self, payload: RawMessageDeleteEvent):
        if payload.channel_id == ids['trainers']:
            data = find(message = payload.message_id)

            if data:
                guild = self.bot.get_guild(ids['guild'])
                member = guild.get_member(data['_id'])
                roles = [guild.get_role(963918497526718535)]

                if member.id == 395249144677007370:
                    role = guild.get_role(968898262570500126)
                    roles.append(role)

                await member.edit(nick = None, roles = roles)
                delete(member.id)

def setup(bot):
    bot.add_cog(Delete(bot))
