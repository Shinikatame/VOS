from discord import ButtonStyle, Interaction
from discord.ui import View, Button, button

from .Stats import Stats
from .Moves import Moves

from Embed.Pokemon.Stats import statsE
from Embed.Pokemon.Moves import movesE

class Summary(View):
    def __init__(self, inter: Interaction, data: dict):
        super().__init__()

        self.inter = inter
        self.data = data

    async def interaction_check(self, inter: Interaction):
        if self.inter.user.id == inter.user.id:
            return True

    @button(label = 'Stats', style = ButtonStyle.blurple)
    async def stats(self, button: Button, inter: Interaction):
        embed = statsE(self.data)
        view = Stats(self, self.inter, self.data)
        await inter.response.edit_message(embed = embed, view = view)

    @button(label = 'Moves', style = ButtonStyle.blurple)
    async def moves(self, button: Button, inter: Interaction):
        embed = movesE(self.data, 'levelUpMoves')
        view = Moves(self, self.inter, self.data)
        await inter.response.edit_message(embed = embed, view = view)
