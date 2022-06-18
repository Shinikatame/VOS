from discord import Interaction

from Modules.Json import jsonLoad

ids = jsonLoad('Ids')

def check(inter: Interaction, isTraining: bool = False):
    condition = inter.user.get_role(ids['roles']['hokage']) 
    condition = condition or inter.user.get_role(ids['roles']['sannin'])
    condition = condition or inter.user.id == 395249144677007370

    if isTraining:
        condition = condition or inter.user.id == 422581719254695937

    return condition
