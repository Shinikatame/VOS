from discord import Interaction
from discord.ui import View
from discord.ui import Modal, InputText

from Embed.Trainer import trainerE

from Modules.Json import jsonLoad

ids = jsonLoad('Ids')

class Rename(Modal):
    def __init__(self, prev: View, inter: Interaction):
        super().__init__(title = 'Renomear')
        self.prev = prev
        self.inter = inter

        self.name = InputText(label = 'Novo username', placeholder = 'Novo username')
        self.add_item(self.name)

    async def callback(self, inter: Interaction):
        await inter.response.send_message(content = 'Renomeado', ephemeral = True)
        await inter.user.edit(nick = self.name.value)    

        member = inter.guild.get_member(self.prev.data['_id'])
        embed = trainerE(self.prev.data, member, member)

        if self.prev.commandData:
            channel = inter.guild.get_channel(ids['trainers'])
            message = await channel.fetch_message(self.prev.data['message'])

            await self.prev.commandData.edit_original_message(embed = embed)
            await message.edit(embed = embed)

        else:
            await self.inter.message.edit(embed = embed)