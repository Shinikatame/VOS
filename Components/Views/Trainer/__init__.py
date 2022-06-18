from discord import Interaction
from discord.ui import View

class Trainers(View):
    def __init__(self, prev: View, inter: Interaction):
        super().__init__(timeout = 15)
        self.prev = prev
        self.inter = inter

    async def on_timeout(self):
        await self.inter.edit_original_message(view = self.prev)
       
    async def interaction_check(self, inter: Interaction):
        if self.inter.user.id == inter.user.id:
            await self.inter.edit_original_message(view = self.prev)
            return True