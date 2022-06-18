from discord import ButtonStyle, Interaction
from discord.ui import View, Button, button

from ..Modals.Registry import Registry as Modal

class Registry(View):
    def __init__(self):
        super().__init__(timeout = None)

    @button(label = 'Registre-se', style = ButtonStyle.blurple, custom_id = 'registry')
    async def registry(self, button: Button, inter: Interaction):
        role = inter.guild.get_role(963918497526718535)
        
        if role in inter.user.roles:
            modal = Modal(inter.client)
            await inter.response.send_modal(modal)

        else:
            await inter.response.send_message(content = 'Você já está registrado.', ephemeral = True)
