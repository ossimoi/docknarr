from ipaddress import ip_address
import yaml

from lib import csgoserver as csgo
from lib import webapi

def get_config():
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
        return cfg

def get_servers(client, server_cfg):
    servers = []
    srv_definitions = {}
    config = get_config()

    with open(config['steam']['serverlist'], 'r') as f:
        try:
            srv_definitions = yaml.load(f)['servers']
        except yaml.YAMLError as err:
            print('Error in server configuration file: {}'.format(err))

    for srv_def in srv_definitions:
        for i in range(srv_def['count']):
            name = srv_def['name'] if srv_def['count'] == 1
                   else srv_def['name'] + str(i+1)
            ip = ip_address(srv_def['ip']) + i
            gslt = _get_gslt(name, steam_cfg)

            s = csgo.CSGOServer(name, ip, gslt, config, client)
            servers.append(s)
    return s

def _get_gslt(sname, steam_cfg):
    api = webapi.API(steam_cfg)
    account_memo = steam_cfg.get('token_prefix', '') + sname
    account_memo_rgx = '^' + account_memo + '$'

    accounts = api.get_game_server_accounts(filter_regex=account_memo_rgx)

    if not accounts:
        resp = api.create_game_server_accounts(730, memo=account_memo)
        return resp[0]['login_token']
    else:
        return accounts[0]['login_token']
