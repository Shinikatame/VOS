from discord import Interaction, ButtonStyle
from discord.ui import View, Button, button

from Embed.Pokemon.Summary import summaryE

class Pokedex(View):
    def __init__(self, prev: View, inter: Interaction, data: dict):
        super().__init__()

        self.prev = prev
        self.inter = inter
        self.data = data

    async def interaction_check(self, inter: Interaction):
        if self.inter.user.id == inter.user.id:
            return True

    @button(label = '←', style = ButtonStyle.red)
    async def back(self, button: Button, inter: Interaction):
        embed = summaryE(self.data)

        await inter.response.edit_message(embed = embed, view = self.prev)