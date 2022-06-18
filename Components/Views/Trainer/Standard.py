from discord import Client, Interaction, ButtonStyle
from discord.ui import View, Button, button

from .Training import Training
from .Promote import Promote

from ...Modals.Trainer.Rename import Rename

from Modules.Json import jsonLoad
from Modules.Check import check

ids = jsonLoad('Ids')

class Standard(View):
    def __init__(self, bot: Client, data: dict, commandData: Interaction = None):
        super().__init__(timeout = None)
        self.bot = bot

        self.data = data
        self.commandData = commandData

        self.isCommand()

    @button(label = 'Promover', custom_id = 'promote', style = ButtonStyle.blurple)
    async def promote(self, button: Button, inter: Interaction):
        if check(inter):
            view = Promote(self, inter)
            await inter.response.edit_message(view = view)

    @button(label = 'Treino', custom_id = 'training', style = ButtonStyle.blurple)
    async def training(self, button: Button, inter: Interaction):
        if check(inter, True):
            view = Training(self, inter)
            await inter.response.edit_message(view = view)

    @button(label = 'Renomear', custom_id = 'rename', style = ButtonStyle.red)
    async def rename(self, button: Button, inter: Interaction):
        if self.data['_id'] == inter.user.id:
            modal = Rename(self, inter)
            await inter.response.send_modal(modal)

    def isCommand(self):
        guild = self.bot.get_guild(ids['guild'])
        member = guild.get_member(self.data['_id'])

        if self.commandData:
            if self.commandData.user.id != member.id:
                self.rename.disabled = True

            if not check(self.commandData):
                self.promote.disabled = True

            if not check(self.commandData, True):
                self.training.disabled = True