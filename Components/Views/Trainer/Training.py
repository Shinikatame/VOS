from discord import Interaction, ButtonStyle
from discord.ui import View, Button, button

from DataBase.Trainers import update

from . import Trainers

from Embed.Trainer import trainerE

from Modules.Json import jsonLoad

ids = jsonLoad('Ids')

class Training(Trainers):
    def __init__(self, prev: View, inter: Interaction):
        super().__init__(prev, inter)
               
    @button(label = 'OU', style = ButtonStyle.green)
    async def over_upper(self, button: Button, inter: Interaction):
        self.prev.data = update(self.prev.data['_id'], 'inc', 'ou', 1)
        await self.edit(inter)

    @button(label = 'OU', style = ButtonStyle.red, row = 1)
    async def over_lower(self, button: Button, inter: Interaction):
        if self.prev.data['ou'] > 0:
            self.prev.data = update(self.prev.data['_id'], 'inc', 'ou', -1)
            await self.edit(inter)

    @button(label = 'UU', style = ButtonStyle.green)
    async def under_upper(self, button: Button, inter: Interaction):
        self.prev.data = update(self.prev.data['_id'], 'inc', 'uu', 1)
        await self.edit(inter)

    @button(label = 'UU', style = ButtonStyle.red, row = 1)
    async def under_lower(self, button: Button, inter: Interaction):
        if self.prev.data['uu'] > 0:
            self.prev.data = update(self.prev.data['_id'], 'inc', 'uu', -1)
            await self.edit(inter)

    @button(label = 'NU', style = ButtonStyle.green)
    async def never_upper(self, button: Button, inter: Interaction):
        self.prev.data = update(self.prev.data['_id'], 'inc', 'nu', 1)
        await self.edit(inter)

    @button(label = 'NU', style = ButtonStyle.red, row = 1)
    async def never_lower(self, button: Button, inter: Interaction):
        if self.prev.data['nu'] > 0:
            self.prev.data = update(self.prev.data['_id'], 'inc', 'nu', -1)
            await self.edit(inter)

    @button(label = 'DB', style = ButtonStyle.green)
    async def doubles_upper(self, button: Button, inter: Interaction):
        self.prev.data = update(self.prev.data['_id'], 'inc', 'db', 1)
        await self.edit(inter)

    @button(label = 'DB', style = ButtonStyle.red, row = 1)
    async def doubles_lower(self, button: Button, inter: Interaction):
        if self.prev.data['db'] > 0:
            self.prev.data = update(self.prev.data['_id'], 'inc', 'db', -1)
            await self.edit(inter)
        
    async def edit(self, inter: Interaction):
        member = inter.guild.get_member(self.prev.data['_id'])
        embed = trainerE(self.prev.data, member, inter.user)

        if self.prev.commandData:
            channel = inter.guild.get_channel(ids['trainers'])
            message = await channel.fetch_message(self.prev.data['message'])

            await self.prev.commandData.edit_original_message(embed = embed)
            await message.edit(embed = embed)

        else:
            await inter.response.edit_message(embed = embed)
