from discord import Embed, Member

from Modules.Json import jsonLoad

from datetime import datetime

ids = jsonLoad('Ids')

def trainerE(data: dict, user: Member, shotter: Member):
    for role in ids['roles'].values():
        role = user.get_role(role)

        if role:
            break

    embed = Embed(color = role.color)

    message = f'**Treinador:** *{user.display_name}*'
    message += f'\n**Cargo:** {role.mention}'
    
    message += f'\n\n**OU:** *{data["ou"]}*'
    message += f'\n**UU:** *{data["uu"]}*'
    message += f'\n**NU:** *{data["nu"]}*'
    message += f'\n**DB:** *{data["db"]}*'

    embed.description = message

    embed.timestamp = datetime.now()
    embed.set_footer(text = shotter.display_name, icon_url = shotter.avatar)

    return embed
