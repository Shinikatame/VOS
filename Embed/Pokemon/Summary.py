from . import pokemonE

evs = {
    'hp': 'Hp',
    'attack': 'Attack',
    'defense': 'Defense',
    'specialattack': 'Sp. attack',
    'specialdefense': 'Sp. defense',
    'speed': 'Speed'
}

def summaryE(data: dict):
    embed = pokemonE(data)
    
    abilities = [v for k, v in data['abilities'].items() if v and k != 'hidden']
    evYields = [f'+{v} {evs[k]}' for k, v in data['evYields'].items() if v != 0]
    gender = [f'{v} {"♂" if k == "male" else "♀"}' for k, v in data['gender'].items()]
    
    embed.add_field(name = 'Abilities', value = '\n'.join(abilities))

    if data['abilities']['hidden']:
        embed.add_field(name = 'Hidden ability', value = data['abilities']['hidden'])

    embed.add_field(name = 'Evs', value = '\n'.join(evYields))
    embed.add_field(name = 'Height', value = f'{data["height"]}m')
    embed.add_field(name = 'Weight', value = f'{data["weight"]}kg')
    embed.add_field(name = 'Egg groups', value = '\n'.join(data['eggGroups']))
    embed.add_field(name = 'Gender', value = '\n'.join(gender))

    if data['heldItems']: 
        embed.add_field(name = 'Held items', value = '\n'.join(data['heldItems']))
    
    embed.add_field(name = 'Tier', value = data['tier'])

    return embed
