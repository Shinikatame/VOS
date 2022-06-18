from discord import Client, slash_command, Interaction
from discord.ext.commands import Cog

from DataBase.Trainers import  update_many, find

from Components.Views.Trainer.Standard import Standard

from Embed.Trainer import trainerE 

from Modules.Json import jsonLoad
from Modules.Check import check

ids = jsonLoad('Ids')

class Reset(Cog):
    def __init__(self, bot: Client):
        self.bot = bot

    @slash_command(name = 'resetar', description = 'Reseta os treinos.')
    async def reset(self, inter: Interaction):
        if check(inter):
            response = await inter.response.send_message('Resetando.', ephemeral = True)

            update_many('set', {'ou': 0, 'uu': 0, 'nu': 0, 'db': 0})
            data = find()
            channel = self.bot.get_channel(ids['trainers'])

            for payload in data:
                message = await channel.fetch_message(payload['message'])
                member = inter.guild.get_member(payload['_id'])
                embed = trainerE(payload, member, inter.user)

                view = Standard(self.bot, payload)
                await message.edit(embed = embed, view = view)

            await response.edit_original_message(content = 'Terminado.')

        else:
            await inter.response.send_message('Você não tem permissão para fazer isso.', ephemeral = True)

def setup(bot):
    bot.add_cog(Reset(bot))
