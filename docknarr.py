#!/usr/bin/env python
import os
import time
import docker
from lib import webapi
from lib import config
from lib import csgoserver as csgo

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
    servers = config.get_servers(client, steam_cfg)
    while True:
        time.sleep(2)
        for s in servers:
            if s.status() != 'running':
                print("{} crashed or not created, fixing...".format(s.name))
                s.start()

if __name__ == "__main__":
    main()
