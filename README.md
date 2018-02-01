# docknarr

ovs-vsctl add-br vsw0  
ovs-vsctl add-port vsw0 eth0  
ovs-vsctl set-port eth0 trunks=341  
  
docker build -t "dregu/csgo:latest"  
  
-- EDIT servers.txt  
./hofnarr.sh  
