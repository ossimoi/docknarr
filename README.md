# docknarr

git clone https://github.com/ponkyh/docknarr.git
cd docknarr
virtualenv -p python3.6 venv
source venv/bin/activate
pip install -Ur requirements.txt
mv servers.txt.example servers.txt
mv config.ini.example config.ini

# Build dockerized CSGO server
git clone https://github.com/Dregu/akl-docker  
cd akl-docker  
docker build -t "dregu/csgo:latest"  
  
-- EDIT servers.txt  
./hofnarr.sh  
