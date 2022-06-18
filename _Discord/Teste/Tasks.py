from discord.ext.commands import Cog
from discord.ext import tasks

class Task(Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.task.start()

    @tasks.loop(seconds = 1)
    async def task(self):
        pass

    @task.before_loop
    async def taskBefore(self):
        pass

    @task.after_loop
    async def taskAfter(self):
        pass

def setup(bot):
    bot.add_cog(Task(bot))