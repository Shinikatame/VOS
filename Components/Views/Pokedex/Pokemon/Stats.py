from discord import Interaction
from discord.ui import View, Button

from . import Pokedex

class Stats(Pokedex):
    def __init__(self, prev: View, inter: Interaction, data: dict):
        super().__init__(prev, inter, data)

        self.add_item(Button(label = 'Smogon', url = self.data['smogonPage']))
        self.add_item(Button(label = 'Serebii', url = self.data['serebiiPage']))
        self.add_item(Button(label = 'Bulbapedia', url = self.data['bulbapediaPage'].replace('_(Pok\u00e9mon)', '')))
