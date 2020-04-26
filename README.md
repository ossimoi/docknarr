# docknarr

Docknarr is a small project to automate management of docker based CS:GO -servers during LAN events.


```
git clone https://github.com/ponkyh/docknarr.git
cd docknarr
virtualenv -p python3.6 venv
source venv/bin/activate
pip install -Ur requirements.txt
mv servers.yml.example servers.yml
mv config.yml.example config.yml

# Do necessary modifications in servers.yml and config.yml

screen ./docknarr.py
```
