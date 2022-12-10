from qtstrap import *
from stagehand.actions import ActionItem
from stagehand.sandbox import SandboxExtension
import discord
import asyncio
import threading


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def my_background_task(self):
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(1234567) # channel ID goes here
        while not self.is_closed():
            counter += 1
            await channel.send(counter)
            await asyncio.sleep(60) # task runs every 60 seconds


discord_client = None


def start_client():
    global discord_client
    intents = discord.Intents.default()
    intents.message_content = True
    discord_client = MyClient(intents=intents)
    discord_client.run('ODM5NzA1NDA5NzM2ODAyMzI0.GoLUUx.tt9lkOas7nzXFB3ZyE65nenaHjQWsmnA2ThqGE')


class DiscordExtension(SandboxExtension):
    name = 'discord'

    def __init__(self):
        self.client_thread = None

    def start_thread(self):
        self.client_thread = threading.Thread(name='Discord', target=start_client, daemon=True)
        self.client_thread.start()

    def send(self, text):
        print(text)


class DiscordWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.token = PersistentLineEdit('discord/token')
        def set_show_token(state):
            if state == Qt.Checked:
                self.token.setEchoMode(QLineEdit.Normal)
            else:
                self.token.setEchoMode(QLineEdit.Password)
        self.show_token = PersistentCheckBox('discord/show_token', changed=set_show_token)
        set_show_token(self.show_token.checkState())

        # self.discord = threading.Thread(name='Web App', target=start_discord, daemon=True)

        with CVBoxLayout(self, align='top') as layout:
            with layout.hbox(align='left'):
                layout.add(QLabel('Discord Token:'))
                layout.add(self.token)
                layout.add(QLabel('Show:'))
                layout.add(self.show_token)
                layout.add(QLabel(), 1)





class DiscordAction(QWidget, ActionItem):
    name = 'discord'

    def __init__(self, changed, owner=None):
        super().__init__()

        self.owner = owner
        with CVBoxLayout(self, margins=0) as layout:
            layout.add(QLabel('Discord'))

    def set_data(self, data):
        pass

    def get_data(self):
        return {}