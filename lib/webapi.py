import os
import re

from steam import WebAPI
from .exceptions import MissingSteamApiKeyError

class API(WebAPI):
    def __init__(self, steam_cfg):
        apikey = os.environ.get('STOOL_STEAMAPI_KEY') or steam_cfg['token']
        if apikey is not None:
            super().__init__(key=apikey)
        else:
            raise MissingSteamApiKeyError('No Steam API key set.')

    def create_game_server_accounts(self, appid, memo='', count=1):
        call = self.IGameServersService.CreateAccount
        return [call(appid=appid, memo=memo)['response'] for i in range(count)]

    # get_game_server_accounts
    def get_game_server_accounts(self, filter_regex=None):
        resp = self.IGameServersService.GetAccountList()['response']['servers']
        if filter_regex is None:
            return resp
        else:
            p = re.compile(filter_regex)
            return list(filter(lambda x: p.search(x.get('memo', '')), resp))
