from discord import Client, Interaction, slash_command, user_command, message_command, Member, Message 
from discord.ext.commands import Cog

class Commands(Cog):
    def __init__(self, bot: Client):
        self.bot = bot

    @slash_command()
    async def slash(self, inter: Interaction):
        pass

    @user_command(guild_ids = [942103135659388958])
    async def user(self, inter: Interaction, member: Member):
        pass

    @message_command(guild_ids = [942103135659388958])
    async def message(self, inter: Interaction, message: Message):
        pass

def setup(bot):
    bot.add_cog(Commands(bot))