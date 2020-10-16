import re

import hoshino
from hoshino import Service

from .utils.util import SQL
from .utils.Steam import get32


sv = Service('SteamStat',bundle='AraraSteamFura')
bindCommand = ['绑定','bind']

@sv.on_message()
async def main(bot, ctx):
    msg = ctx['raw_message'].split(' ')
    if re.match('ara',msg[0].lower()):
        length = len(msg)
        if length >= 2:
            if msg[1] in bindCommand:
                if length == 4:
                    r = SQL('users')
                    sender = str(ctx['user_id'])
                    if not r.get(sender):
                        r[sender] = {}
                    if not r.get(sender).get(msg[2]):
                        s_id = await get32(msg[3])
                        await bot.send(ctx,'唔，尝试把呼唤{}的咒语改成{}'.format(str(s_id),msg[2]))
                        r[sender] = r.get('sender').update({msg[2]:s_id}) if r.get('sender') else {msg[2]:s_id}
                        await bot.send(ctx,'完成了！')
                    else:
                        await bot.send(ctx,'{}的魔法已经存在了？我记得原来是叫{}来着'.format(msg[2],str(r.get(sender).get(msg[2]))))
                else:
                    await bot.send(ctx,'缺少参数的话就连我这样的魔女也没有办法呀\n /自定义名字/ /bot/')