import json
import random

from khl import TextMsg, Bot, Cert

# load config from config/config.json, replace `path` points to your own config file
# config template: `./config/config.json.example`
with open('./config/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# init Cert for Bot OAuth
cert = Cert(client_id=config['client_id'],
            client_secret=config['client_secret'],
            token=config['token'])

# init Bot
bot = Bot(cmd_prefix=['!', '！'], cert=cert)


# register command
# invoke this via saying `!roll 1 100` in channel
# or `!roll 1 100 5` to dice 5 times once
@bot.command(name='roll')
async def roll(msg: TextMsg, t_min: str, t_max: str, n: str = 1):
    result = [random.randint(int(t_min), int(t_max)) for i in range(int(n))]
    await msg.reply(f'you got:{result}')


# everything done, go ahead now!
bot.run()
