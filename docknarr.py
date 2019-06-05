#!/usr/bin/env python
import os
import time
from docker import from_env
from docker.errors import BuildError, ImageNotFound

from time import localtime, asctime
from lib import webapi
from lib import config
from lib import csgoserver as csgo
from halo import Halo

def _build_image(server):
    with Halo(text=f'Image {server.image} not found, building...',
              spinner='arc') as spin:
        try:
            server.build_image()
        except BuildError as e:
            spin.fail(text=f'Building image {server.image} failed!')
            print(e)
            return False
        else:
            spin.succeed(text=f'Image {server.image} built!')

def main():
    ct = lambda: asctime(localtime())

    with Halo(text='Initializing configuration...', spinner='arc'):
        steam_cfg = config.get_config()['steam']
        docker_cfg = config.get_config()['docker']
    with Halo(text='Getting docker client...', spinner='arc'):
        client = from_env()
    with Halo(text='Configuring servers...', spinner='arc'):
        servers = config.get_servers(client, steam_cfg)

    while True:
        time.sleep(2)
        for s in servers:
            if s.status() != 'running':
                print(f'{ct()}  {s.name} crashed or not created, fixing...')
                try:
                    s.start()
                except ImageNotFound:
                    _build_image(s)
                    s.start()
                    print(f'{ct()}  {s.name} started...')

if __name__ == "__main__":
    main()
