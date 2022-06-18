from discord import Client, Member
from discord.ext.commands import Cog

from DataBase.Trainers import delete, find

from Modules.MessageDelete import messageDelete, messagesDeleteLoop

from Modules.Json import jsonLoad

ids = jsonLoad('Ids')

class TrainersDelete(Cog):
    def __init__(self, bot: Client):
        self.bot = bot

    @Cog.listener('on_member_remove')
    async def leave(self, member: Member):
        await messageDelete(member, find, ids['trainers'])
        delete(member.id)

    @Cog.listener('on_ready')
    async def checking(self):
        if not self.bot.is_ready():
            await self.bot.wait_until_ready()

        await messagesDeleteLoop(self.bot, find(), ids['trainers'], delete)
    
def setup(bot):
    bot.add_cog(TrainersDelete(bot))