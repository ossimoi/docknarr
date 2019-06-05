#!/usr/bin/env python
import os
import time
import docker

from time import localtime, asctime
from lib import webapi
from lib import config
from lib import csgoserver as csgo

def main():
    steam_cfg = config.get_config()['steam']
    docker_cfg = config.get_config()['docker']
    client = docker.from_env()
    servers = config.get_servers(client, steam_cfg)

    ct = lambda: asctime(localtime())

    while True:
        time.sleep(2)
        for s in servers:
            if s.status() != 'running':
                print(f'{ct()}  {s.name} crashed or not created, fixing...')
                s.start()
                print(f'{ct()}  {s.name} started...)

if __name__ == "__main__":
    main()
