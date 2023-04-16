from discord import Intents
from discord.ext.commands import Bot

from dotenv import load_dotenv
from os import getenv, listdir

load_dotenv('.env')

class Client(Bot):
    def __init__(self):
        super().__init__(intents = Intents.all())

        self.cogs()
        self.run(getenv('VOS_TOKEN'))

    def cogs(self, path = '_Discord'):
        for file in listdir(path):
            if file != '__pycache__':
                if file.endswith('.py'):
                    file = f'{path}.{file}'.replace('.py', '')
                    self.load_extension(file.replace('/', '.'))

                else:
                    self.cogs(path + '/' + file)

if __name__ == '__main__':
    Client()