from discord.ui import View, Button

class Move(View):
    def __init__(self, data: dict):
        super().__init__()

        self.add_item(Button(label = 'Smogon', url = data['smogonPage']))
        self.add_item(Button(label = 'Serebii', url = data['serebiiPage']))
        self.add_item(Button(label = 'Bulbapedia', url = data['bulbapediaPage'].replace('_(move)', '')))
