from discord import Interaction, SelectOption
from discord.ui import View, Select, select

from . import Trainers

from Embed.Trainer import trainerE

from Modules.Json import jsonLoad

ids = jsonLoad('Ids')

class Promote(Trainers):
    def __init__(self, prev: View, inter: Interaction):
        super().__init__(prev, inter)
        self.prev = prev

        roles = ids['roles'].copy()
        roles.pop('hokage')

        self.select.options = [SelectOption(label = k.capitalize(), value = f'{v}') for k, v in roles.items()]

    @select(placeholder = 'Promover')
    async def select(self, select: Select, inter: Interaction):
        member = inter.guild.get_member(self.prev.data['_id'])

        role = inter.guild.get_role(int(select.values[0]))
        await member.add_roles(role)
        
        for option in select.options:
            if option.value != select.values[0]:
                role = member.get_role(int(option.value))

                if role:
                    await member.remove_roles(role)
                    break

        embed = trainerE(self.prev.data, member, inter.user)

        if self.prev.commandData:
            channel = inter.guild.get_channel(ids['trainers'])
            message = await channel.fetch_message(self.prev.data['message'])

            await self.prev.commandData.edit_original_message(embed = embed)
            await message.edit(embed = embed)

        else:
            await inter.response.edit_message(embed = embed)
            