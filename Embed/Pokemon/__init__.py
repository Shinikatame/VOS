from discord import Embed, Colour

def pokemonE(data: dict):
    embed = Embed(colour = Colour(data['color']))

    embed.title = f'`{data["_id"]}` {data["species"].capitalize()}'
    embed.set_image(url = data['sprite'])

    url = f'https://raw.githubusercontent.com/Shinikatame/ayumin/master/VOS/Images/Types/'
    types = '-'.join(data['types'])
    embed.set_thumbnail(url = url + f'{types}.png')
    
    return embed
