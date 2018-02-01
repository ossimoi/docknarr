# docknarr

ovs-vsctl add-br vsw0
ovs-vsctl add-port vsw0 eth0
ovs-vsctl set-port eth0 trunks=341

docker pull dregu/csgo

-- EDIT servers.txt
./hofnarr.sh
