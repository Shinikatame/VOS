from discord import Member, Client

from typing import Callable

from Modules.Json import jsonLoad

ids = jsonLoad('Ids')

async def messageDelete(member: Member, function: Callable, channel: int):
    data = function(member.id)
    channel = member.guild.get_channel(channel)

    if channel:
        try: message = await channel.fetch_message(data['message'])

        except: return
        
        else: await message.delete()

async def messagesDeleteLoop(bot: Client, data: list, channel: int, function: Callable):
    guild = bot.get_guild(ids['guild'])
    channel = guild.get_channel(channel)

    for payload in data:
        member = guild.get_member(payload['_id'])

        if not member:
            try: message = await channel.fetch_message(payload['message'])

            except: pass

            else:
                await message.delete()
                
                function(payload['_id'])
