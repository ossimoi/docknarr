# docknarr

git clone https://github.com/ponkyh/docknarr.git  
cd docknarr  
virtualenv -p python3.6 venv  
source venv/bin/activate  
pip install -Ur requirements.txt  
mv servers.txt.example servers.txt  
mv config.ini.example config.ini  

### Do necessary modifications in servers.txt and config.ini  

./docknarr.py

