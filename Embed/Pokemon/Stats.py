from . import pokemonE

def statsE(data: dict):
    embed = pokemonE(data)
    embed.description = '**Status base**\n\n'

    embed.description += f'`{data["baseStats"]["hp"]}` - **HP**\n'
    embed.description += f'`{data["baseStats"]["attack"]}` - **Attack**\n'
    embed.description += f'`{data["baseStats"]["defense"]}` - **Defense**\n'
    embed.description += f'`{data["baseStats"]["specialattack"]}` - **Special attack**\n'
    embed.description += f'`{data["baseStats"]["specialdefense"]}` - **Special defense**\n'
    embed.description += f'`{data["baseStats"]["speed"]}` - **Speed**\n\n'

    embed.description += f' **Total** - `{data["baseStatsTotal"]}`'

    return embed
