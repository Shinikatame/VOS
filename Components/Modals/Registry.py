from discord import Client, Interaction
from discord.ui import Modal, InputText

from DataBase.Trainers import insert_one, find

from Components.Views.Trainer.Standard import Standard

from Embed.Trainer import trainerE 

from Modules.Json import jsonLoad

ids = jsonLoad('Ids')

class Registry(Modal):
    def __init__(self, bot: Client):
        super().__init__(title = 'Registro')
        self.bot = bot

        self.name = InputText(label = 'Username do PokeMMO', placeholder = 'username')
        self.add_item(self.name)

    async def callback(self, inter: Interaction):
        await inter.response.send_message(content = 'Registrado', ephemeral = True)

        roles = [inter.guild.get_role(ids['roles']['gennin'])]

        await inter.user.edit(nick = self.name.value, roles = roles)
        
        user = inter.guild.get_member(inter.user.id)
        client = inter.guild.get_member(inter.client.user.id)

        channel = inter.guild.get_channel(ids['trainers'])

        message = await channel.send('⠀⠀⠀⠀⠀⠀⠀⠀⠀')

        data = {
            '_id': inter.user.id,
            'message': message.id,
            'ou': 0,
            'uu': 0,
            'nu': 0,
            'db': 0
        }

        view = Standard(inter.client ,data)
        embed = trainerE(data, user, client)
        await message.edit(view = view, embed = embed)
        
        insert_one(inter.user.id, message.id)