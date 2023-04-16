from discord import Client, slash_command, Interaction, Member, Option
from discord.ext.commands import Cog

from DataBase.Trainers import  find

from Components.Views.Trainer.Standard import Standard

from Embed.Trainer import trainerE 

class Trainer(Cog):
    def __init__(self, bot: Client):
        self.bot = bot

    @slash_command(name = 'treinador', description = 'Procure um treinador.')
    async def trainer(self, inter: Interaction, 
    user: Option(Member, name = 'membro', description = 'Quem você quer procurar?', default = None)):
        member = user or inter.user
        data = find(member.id)
        
        embed = trainerE(data, member, inter.user)
        response = await inter.response.send_message(f'{member.mention} **{member.display_name}**', embed = embed, ephemeral = True)

        view = Standard(self.bot, data, response)
        await response.edit_original_message(view = view)

def setup(bot):
    bot.add_cog(Trainer(bot))
