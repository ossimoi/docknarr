import os
from steam import WebAPI

from . import config
from .exceptions import MissingSteamApiKeyError

c = config.get_config('steam')

class Api(WebAPI):
    def __init__(self):
        apikey = os.environ.get('STOOL_STEAMAPI_KEY') or c['token']
        if apikey is not None:
            super().__init__(key=apikey)
        else:
            raise MissingSteamApiKeyError('No Steam API key set.')

    def create_game_server_accounts(self, appid, memo='', count=1):
        call = self.IGameServersService.CreateAccount
        return [call(appid=appid, memo=memo)['response'] for i in range(count)]

    # get_game_server_accounts
    def get_game_server_accounts(self):
        return self.IGameServersService.GetAccountList()['response']

