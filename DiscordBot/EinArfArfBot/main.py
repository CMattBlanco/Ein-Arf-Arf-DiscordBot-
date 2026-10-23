import random
import datetime
from zoneinfo import ZoneInfo
import discord
from discord.ext import tasks

TZ = ZoneInfo('Asia/Manila')
MORNING_TIME = datetime.time(hour=5, minute=45, tzinfo=TZ)   
NIGHT_TIME = datetime.time(hour=22, minute=0, tzinfo=TZ)     

CHANNEL_ID = 1234567890  


MORNING_MESSAGE = 'AWOOOO!! MGA TANG INA NYOOOO, GUMISING NA KAYOOOO MGA BUSENG ☀️'
MORNING_GIF = 'https://tenor.com/view/gelo-cruz-good-morning-gelo-cruz-good-morning-gif-5276284868924360896'

NIGHT_MESSAGE = 'AWOOOO!! MGA TANG INA NYOOOO, KELAN PA KAYO MATUTULOG MGA BUSENG🌙'
NIGHT_GIF = 'https://tenor.com/view/gelo-cruz-good-night-gelo-cruz-good-night-gif-4565869440459472284'  # change to a different GIF if you like

ADVICE_RESPONSES = [
    'Tangina MO nananahimik ako rito Bat mo ko iniistorbo sa problema mo buseng?!',
    'ARF! ARF! me no habla speak Tagalog..... PUKINANGINAMO ARF! ARF!',
    'AWOOOO!! Baka TANGA KA LANG AWOOOOO!!!!',
    'Gusto mo kagatin nalang kita tol HA?!! sinira mo yung tulog ko sa kalye',
    'Tol.... muka mo palang, problema na eh',
    'IKAW NANANMAN?!! WAG KANA MAGTANONG SAKEN NG DI KO PROBLEMA, MAS AMAW',
    'Advice? what is that? its a girl group anak ',
    'Ipasa mo nalang problema mo ANIMAL',
    'HA? di ko marinig yung tanong mo',
    'alam mo tol, Biniyayaan ka ng maykapal ng kokoteng hindi kayang maarok kahit ang pinakasimpleng mga bagay such as ang problema mo',
    'anak, ang advice ay parang aso, di tinatanong yan kinakantot yan',
    'sasagutin ko yan... kung bibigyan mo ko ng diaper',
    'di ka makakapasa kasi bobo ka',
    'TANG INA MO GINAGAWA MO KONG SPAM',
]

LOVE_ADVICE_RESPONSES = [
    'anak, ang pagmamaha'
]

class Client(discord.Client):
    async def setup_hook(self):
        self.morning_greeting.start()
        self.night_greeting.start()

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        content = message.content.lower()

        if 'hello' in content:
            await message.channel.send(f'AWOOOO!!! TANG INA MOOOOO, Wala kong pake sa hello moooo!!! {message.author}')

        elif 'pakyu' in content:
            await message.channel.send(f'AWOOOO!!! pakyu sayo kapatid na {message.author} ')

        # Random reply when "advice" appears anywhere in the message
        elif 'advice' in content:
            await message.channel.send(f'{message.author.mention} {random.choice(ADVICE_RESPONSES)}')

        elif 'love advice' in content:
            await message.channel.send(f'{message.author.mention} {random.choice(ADVICE_RESPONSES)}')

        elif 'career advice' in content:
            await message.channel.send(f'{message.author.mention} {random.choice(ADVICE_RESPONSES)}')

        elif 'financial advice' in content:
            await message.channel.send(f'{message.author.mention} {random.choice(ADVICE_RESPONSES)}')

        elif '!time' in content or 'what time' in content or 'anong oras' in content:
            now = datetime.datetime.now(TZ)
            time_str = now.strftime('%I:%M %p').lstrip('0')   
            date_str = now.strftime('%A, %B %d, %Y')          
            await message.channel.send(
                f'AWOOOO!! {message.author.mention}, ang oras sa Pilipinas ngayon ay **{time_str}** 🇵🇭\n'
                f' {date_str}'
            )

        

    async def on_message_delete(self, message):
        if message.author.bot:
            return

        await message.channel.send(
            f'{message.author.mention} deleted a message: "{message.content}"'
        )


    @tasks.loop(time=MORNING_TIME)
    async def morning_greeting(self):
        channel = self.get_channel(CHANNEL_ID)
        if channel is not None:
            await channel.send(MORNING_MESSAGE)
            await channel.send(MORNING_GIF)

    @tasks.loop(time=NIGHT_TIME)
    async def night_greeting(self):
        channel = self.get_channel(CHANNEL_ID)
        if channel is not None:
            await channel.send(NIGHT_MESSAGE)
            await channel.send(NIGHT_GIF)

    @morning_greeting.before_loop
    @night_greeting.before_loop
    async def wait_for_ready(self):
        await self.wait_until_ready()


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run('SAMPLE TOKEN')





