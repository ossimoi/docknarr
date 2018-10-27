#!/usr/bin/env python
import os
import time
import docker
from lib import webapi
from lib import config
from lib import csgoserver as csgo

def get_servers(client, steam_cfg):
    servers = []
    with open (steam_cfg['serverlist']) as f:
        content = f.readlines()
        for line in content:
            ip = line.split()[0]
            name = line.split()[1]
            s = csgo.CSGOServer(name, ip, get_token(name, steam_cfg), config.get_config(), client)
            servers.append(s)
    return servers

def get_token(sname, steam_cfg):
    api = webapi.API(steam_cfg)
    tokens = api.get_game_server_accounts()
    prefix = steam_cfg['token_prefix']
    for k, v in tokens.items():
        if isinstance(v, list):
            for token in v:
                if 'memo' in token:
                    if token['memo'] == prefix + sname:
                        return token
    return api.create_game_server_accounts(730, prefix + sname)

def build_image(client, docker_cfg):
    try:
        client.images.get('docknarr')
    except docker.errors.ImageNotFound:
        print("No image found, building...")
        df = docker_cfg['dockerfile']
        path = os.path.dirname(df)
        client.images.build(path=path, dockerfile='Dockerfile', tag='docknarr', quiet=False)

def main():
    steam_cfg = config.get_config()['steam']
    docker_cfg = config.get_config()['docker']
    client = docker.from_env()
    build_image(client, docker_cfg)
    servers = get_servers(client, steam_cfg)
    while True:
        time.sleep(2)
        for s in servers:
            if s.status() != 'running':
                print("{} crashed or not created, fixing...".format(s.name))
                s.start()

if __name__ == "__main__":
    main()
