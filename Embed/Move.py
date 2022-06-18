from discord import Embed, Colour

colours = {
    'Bug': Colour(9552424),
    'Dark': Colour(5919334),
    'Dragon': Colour(224709),
    'Electric': Colour(15979320),
    'Fighting': Colour(13581929),
    'Fire': Colour(16751955),
    'Flying': Colour(9480926),
    'Ghost': Colour(5335470),
    'Grass': Colour(6536283),
    'Ground': Colour(14317636),
    'Ice': Colour(7720897),
    'Normal': Colour(9542306),
    'Poison': Colour(11299529),
    'Psychic': Colour(16347767),
    'Rock': Colour(13154444),
    'Steel': Colour(5935010),
    'Water': Colour(5018070)
}

def moveE(data: dict):
    embed = Embed(colour = colours[data['type']])

    embed.title = data['name']
    embed.description = data['shortDesc']

    url = f'https://raw.githubusercontent.com/Shinikatame/ayumin/master/VOS/Images/Category/'
    category = f'{data["type"]}-{data["category"]}'
    embed.set_thumbnail(url = url + f'{category}.png')

    embed.add_field(name = 'Poder', value = data['basePower'], inline = True)
    embed.add_field(name = 'Precisão', value = data['accuracy'], inline = True)
    embed.add_field(name = 'PP', value = data['pp'], inline = True)
    embed.add_field(name = 'Prioridade', value = data['priority'], inline = True)
    embed.add_field(name = 'Alvos', value = data['target'], inline = True)

    return embed
