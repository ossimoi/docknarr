#!/bin/bash

#######
#
# hofnarr.sh kynyskripti
# (c) Ossi & Ossi #tunk
#
# konffaa seuraavat jos osaat
#
#######

SERVERLIST="servers.txt"
RCONPW="TurboHofnarri"
TICKRATE=128
MAP=de_dust2
MAPGROUP=mg_active
MAXPLAYERS=16
GAMEMODE=1
GAMETYPE=0
ENTRYPOINT=/home/cs/start
MASK="/24"
GATEWAY="85.188.59.1"
VLAN="341"

mkdir -p -m a+rw /home/cs/matches

cat $SERVERLIST | while read line
do
    IP=$(echo $line |awk ' { print $1 } ')
    GSLT=$(echo $line | awk ' { print $2 } ')
    NAME=$(echo $line | awk ' { print $3 } ')
    
    docker ps | grep -wq ${NAME}
    if [ $? -eq 0 ] ; then
      echo "${NAME} already running..."
    else
      docker run -dti --net="none" --name="${NAME}" -h "${NAME}" --privileged=true -v /home/cs/matches:/home/cs/serverfiles/csgo/matches -e TICKRATE="${TICKRATE}" -e GSLT="${GSLT}" -e MAP="${MAP}" -e MAXPLAYERS="${MAXPLAYERS}" -e MAPGROUP=${MAPGROUP} -e GAMEMODE=${GAMEMODE} -e GAMETYPE=${GAMETYPE} -e HOSTNAME=${NAME} -e RCONPASSWORD=${RCONPW} -e PUBLIC=${IP} --entrypoint ${ENTRYPOINT} dregu/csgo
      ovs-docker add-port vsw0 eth0 ${NAME} --ipaddress=${IP}${MASK} --gateway=${GATEWAY}
      ovs-docker set-vlan vsw0 eth0 ${NAME} ${VLAN}
    fi

done

