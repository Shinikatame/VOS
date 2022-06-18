from discord import SlashCommandGroup, Client, Interaction, AutocompleteContext, Option
from discord.ext.commands import Cog

from Components.Views.Pokedex.Pokemon.Summary import Summary
from Components.Views.Pokedex.Move import Move

from Embed.Pokemon.Summary import summaryE
from Embed.Move import moveE

from DataBase.Pokedex import find

from Modules.Json import jsonLoad
from Modules.Choices import choices

ids = jsonLoad('Ids')
pokemons = jsonLoad('Pokedex')
moves = jsonLoad('Moves')
    
async def getPokemon(ctx: AutocompleteContext):
    return [poke for poke in pokemons if ctx.value.lower() in poke.lower()]

async def getMove(ctx: AutocompleteContext):
    return [move for move in moves if ctx.value.lower() in move.lower()]

class Pokedex(Cog):
    group = SlashCommandGroup('pokedex', 'Pokedex do PokeMMO.')
    
    def __init__(self, bot: Client):
        self.bot = bot

    @group.command(description = 'Pokedex do PokeMMO.')
    async def pokemon(self, inter: Interaction, search: Option(str, autocomplete = getPokemon), hidden: Option(str, default = False, choices = choices())):
        if search in pokemons:
            data = find(search.lower())
            embed = summaryE(data)
            view = Summary(inter, data)

            await inter.response.send_message(embed = embed, view = view, ephemeral = True if hidden == 'on' else False)

        else:
            await inter.response.send_message('Pokemon não encontrado', ephemeral = True)

    @group.command(description = 'Movimentos pokemon.')
    async def movement(self, inter: Interaction, search: Option(str, autocomplete = getMove), hidden: Option(str, default = False, choices = choices())):
        if search in moves:
            data = jsonLoad(f'Pokedex/Moves/{search}')
            embed = moveE(data)
            view = Move(data)
        
            await inter.response.send_message(embed = embed, view = view, ephemeral = True if hidden == 'on' else False)

        else:
            await inter.response.send_message('Movimento não encontrado', ephemeral = True)

def setup(bot):
    bot.add_cog(Pokedex(bot))
