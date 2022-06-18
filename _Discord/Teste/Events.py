from discord import Client, Message
from discord.raw_models import RawMessageUpdateEvent
from discord.ext.commands import Cog

class Events(Cog):
    def __init__(self, bot: Client):
        self.bot = bot

    @Cog.listener('on_ready')
    async def ready(self):
        pass

    @Cog.listener('on_message')
    async def message(self, message: Message):
        pass

    @Cog.listener('on_raw_message_edit')
    async def messageEdit(self, payload: RawMessageUpdateEvent):
        pass

    @Cog.listener('on_raw_bulk_message_delete')
    async def messagesdelete(self, payload):
        pass

    @Cog.listener('on_raw_message_delete')
    async def messagedelete(self, payload):
        pass

def setup(bot):
    bot.add_cog(Events(bot))
