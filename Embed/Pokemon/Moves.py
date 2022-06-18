from . import pokemonE

from Modules.Json import jsonLoad

title = {
    'levelUpMoves': 'Level Up',
    'tmMoves': 'TMs&HMs', 
    'tutorMoves': 'Tutor',
    'eggMoves': 'Egg'
}

def movesE(data: dict, path: str):
    embed = pokemonE(data)

    data: list = data['getLearnset'][path]

    embed.description = f'***{title[path]} Moves***\n\n'

    if path == 'levelUpMoves':
        data.sort(key = lambda x: x['level'])

    for move in data:
        dataMove = jsonLoad(f'Pokedex/Moves/{move["name"]}')

        if 'level' in move:
            level = f'0{move["level"]}' if move['level'] < 10 else move['level']
            embed.description += f'`lv. {level}` **{move["name"]}**\n'
        
        else:
            embed.description += f'***{move["name"]}***\n'

        embed.description += f'**{dataMove["type"]} | {dataMove["category"]}**\n'
        embed.description += f'**Power** `{dataMove["basePower"]}` | **Accuracy** `{dataMove["accuracy"]}` | **Priority** `{dataMove["priority"]}` | **PP** `{dataMove["pp"]}`\n\n'
                    
    return embed
