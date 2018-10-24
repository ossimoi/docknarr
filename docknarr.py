#!/usr/bin/env python
import os
import docker
from lib import webapi
from lib import config

s_cfg = config.get_config('steam')
a = webapi.Api()

def getServers():
    servers = []
    with open (s_cfg['serverlist']) as f:
        content = f.readlines()
        for line in content:
            ip = line.split()[0]
            sname = line.split()[1]
            s = {'name': sname, 'ip': ip}
            servers.append(dict(s))
    return servers

def getToken(sname):
    tDict = a.get_game_server_accounts()
    for k, v in tDict.items():
        if isinstance(v, list):
            for token in v:
                if 'memo' in token:
                    if token['memo'] == s_cfg['token_prefix'] + sname:
                        return token
    return a.create_game_server_accounts(730, s_cfg['token_prefix'] + sname)

def startServers(servers):
    client = docker.from_env()
    cs_cfg = config.get_config('cs')
    d_cfg = config.get_config('docker')
    try:
        client.images.get('docknarr')
    except docker.errors.ImageNotFound:
        print("No image found, building...")
        df = './Dockerfile'
        path = os.path.dirname(df)
        client.images.build(path=path, dockerfile='Dockerfile', quiet=False)
    for s in servers:
        sname = s['name']
        ip = s['ip']
        token = getToken(sname)
        env = {
                'TICKRATE': cs_cfg['tickrate'],
                'GSLT': token,
                'MAP': cs_cfg['map'],
                'MAXPLAYERS': cs_cfg['maxplayers'],
                'MAPGROUP': cs_cfg['mapgroup'],
                'GAMEMODE': cs_cfg['gamemode'],
                'GAMETYPE': cs_cfg['gametype'],
                'HOSTNAME': sname,
                'RCONPW': cs_cfg['rcon_pw'],
                'IP': ip
                }
        vols = {
                '/home/ponky/cs/matches': {
                    'bind': '/home/cs/serverfiles/csgo/matches',
                    'mode': 'rw'
                    }
                }
        client.containers.run(
                image='docknarr',
                name=sname,
                network_mode='host',
                entrypoint=d_cfg['entrypoint'],
                volumes=vols,
                environment=env,
                privileged=True,
                detach=True
                )

def main():
    startServers(getServers())

if __name__ == "__main__":
    main()
