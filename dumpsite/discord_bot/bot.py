import discord
import os

from dotenv import load_dotenv
load_dotenv()

class MyClient(discord.Client):
    async def on_connect(self):
        print('Connecting to Discord!')

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        print(f'Total number of users: {len(set(self.get_all_members()))}')

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('!test_bot'):
            if len(message.content.split(' ')) == 1:
                text_message = '''
                ```
                Congratulations on using this bot!
                
                It'll work wonders for you!
                ```
                '''
                await message.channel.send(text_message)
            
            elif message.content.split(' ')[1] == 'help':
                await message.channel.send('This is the help page for my bot.')
            
            elif message.content.split(' ')[1] == 'members':
                data = set(self.get_all_members())
                for user in data:
                    await message.channel.send(user.mention)
            
            elif message.content.split(' ')[1] == 'ping':
                try:
                    for i in range(int(message.content.split(' ')[2])):
                        await message.channel.send('Ping from me!')
                except:
                    await message.channel.send('Request not valid!')
        
        else:
            await message.channel.send(f'{message.author.mention} sent a message : {message.content}')

client = MyClient()
client.run(os.getenv('CLIENT_TOKEN'))
