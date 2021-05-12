from qtstrap import *
from stagehand.actions import ActionStackItem
# import discord
import asyncio


# class MyClient(discord.Client):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # create the background task and run it in the background
#         self.bg_task = self.loop.create_task(self.my_background_task())

#     async def on_ready(self):
#         print(f'Logged in as {self.user} (ID: {self.user.id})')
#         print('------')

#     async def my_background_task(self):
#         await self.wait_until_ready()
#         counter = 0
#         channel = self.get_channel(1234567) # channel ID goes here
#         while not self.is_closed():
#             counter += 1
#             await channel.send(counter)
#             await asyncio.sleep(60) # task runs every 60 seconds


class DiscordExtension:
    def __init__(self):
        pass

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





class DiscordAction(QWidget, ActionStackItem):
    def __init__(self, changed):
        super().__init__()

        with CVBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('Discord'))

    def from_dict(self, data):
        pass

    def to_dict(self):
        return {}


def install_plugin(plugin_manager):
    plugin_manager.register.action('discord', DiscordAction)

    plugin_manager.register.sandbox_extension('discord', DiscordExtension())

    plugin_manager.register.widget('Discord', DiscordWidget())