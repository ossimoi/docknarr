# docknarr

Docknarr is a small project to automate management of docker based CS:GO -servers during LAN events. This script is mainly used in Finnish LAN events. Some important things to note before running CS:GO in docker:

- Each server requires GSLT token if non-RFC1918 IP-address is used
- GSLT wont work if you connect through a NAT

This is why we pass host networking to each container so that each individual server instance can bind to specific IP-address, which is added to host interface.

```
git clone https://github.com/ponkyh/docknarr.git
cd docknarr
virtualenv -p python3.6 venv
source venv/bin/activate
pip install -Ur requirements.txt
mv servers.txt.example servers.txt
mv config.ini.example config.ini

# Do necessary modifications in servers.txt and config.ini

screen ./docknarr.py
´´´
