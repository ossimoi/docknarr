#!/usr/bin/env python
import os
import time
import docker

from lib import webapi
from lib import config
from lib import csgoserver as csgo

def main():
    steam_cfg = config.get_config()['steam']
    docker_cfg = config.get_config()['docker']
    client = docker.from_env()
    servers = config.get_servers(client, steam_cfg)

    while True:
        time.sleep(2)
        for s in servers:
            if s.status() != 'running':
                print("{} crashed or not created, fixing...".format(s.name))
                s.start()

if __name__ == "__main__":
    main()
