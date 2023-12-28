from configparser import ConfigParser
from pypresence import Presence
import time

def create_default_rpc_config():
    config = ConfigParser()
    config['Settings'] = {
        'client': '1190018099244707911',
        'state': 'VimeWorld.com',
        'details': 'VimeWorld.com',
        'buttons_one_txt': '',
        'buttons_one_url': '',
        'large_image': '',
        'large_text': '',
        'small_image': '',
        'small_text': ''
    }

    with open('rpc.conf', 'w') as configfile:
        config.write(configfile)

def read_rpc_config():
    config = ConfigParser()
    config.read('rpc.conf')

    settings = {
        'client': config.get('Settings', 'client', fallback=None),
        'state': config.get('Settings', 'state', fallback=None),
        'details': config.get('Settings', 'details', fallback=None),
        'buttons_one_txt': config.get('Settings', 'buttons_one_txt', fallback=None),
        'buttons_one_url': config.get('Settings', 'buttons_one_url', fallback=None),
        'large_image': config.get('Settings', 'large_image', fallback=None),
        'small_text': config.get('Settings', 'small_text', fallback=None)
    }

    return settings

def update_presence():
    settings = read_rpc_config()
    
    client = settings['client']
    RPC = Presence(client)
    RPC.connect()

    buttons = [{"label": "Trigger", "url": "https://github.com/Wonkiest29/trigger"}]

    if settings['buttons_one_txt'] and settings['buttons_one_url']:
        new_button = {"label": settings['buttons_one_txt'], "url": settings['buttons_one_url']}
        buttons.append(new_button)

    large_image = settings['large_image']
    small_text = settings['small_text']
    presence_args = {
        'state': settings['state'],
        'details': settings['details'],
        'buttons': buttons,
    }

    if large_image:
        presence_args['large_image'] = large_image
    if small_text:
        presence_args['small_text'] = small_text

    RPC.update(**presence_args)

    while True:
        RPC.update(**presence_args)
        time.sleep(15)

try:
    with open('rpc.conf', 'r'):
        pass
except FileNotFoundError:
    create_default_rpc_config()

if __name__ == "__main__":
    update_presence()
