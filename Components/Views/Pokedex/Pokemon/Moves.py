from discord import ButtonStyle, Interaction
from discord.ui import View, Button, button

from . import Pokedex

from Embed.Pokemon.Moves import movesE

class Moves(Pokedex):
    def __init__(self, prev: View, inter: Interaction, data: dict):
        super().__init__(prev, inter, data)
        self.data = data
        self.level.disabled = True

        self.methods = {
            'levelUpMoves': self.level,
            'tmMoves': self.tms_hms,
            'tutorMoves': self.tutor,
            'eggMoves': self.egg
        }

        self.disable()

    @button(label = 'Level', style = ButtonStyle.blurple)
    async def level(self, button: Button, inter: Interaction):
        await self.payload(button, inter, 'levelUpMoves')

    @button(label = 'TMs&HMs', style = ButtonStyle.blurple)
    async def tms_hms(self, button: Button, inter: Interaction):
        await self.payload(button, inter, 'tmMoves')

    @button(label = 'Tutor', style = ButtonStyle.blurple)
    async def tutor(self, button: Button, inter: Interaction):
        await self.payload(button, inter, 'tutorMoves')

    @button(label = 'Egg', style = ButtonStyle.blurple)
    async def egg(self, button: Button, inter: Interaction):
        await self.payload(button, inter, 'eggMoves')

    async def payload(self, button: Button, inter: Interaction, type: str):
        self.enable_all_items()
        button.disabled = True

        self.disable()

        embed = movesE(self.data, type)
        await inter.response.edit_message(embed = embed, view = self)

    def disable(self):
        for key, value in self.data['getLearnset'].items():
            if not value:
                button: Button = self.methods[key]
                button.style = ButtonStyle.gray
                button.disabled = True