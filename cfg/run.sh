#!/bin/bash
/home/csgo/csgoserver/srcds_run -console -usercon +game_type 0 +game_mode 1 +mapgroup mg_active +map ${MAP} -tickrate 128 +sv_setsteamaccount ${GSLT} +rcon_password ${RCONPW} -maxplayer_override ${MAXPLAYERS} -ip ${IP} +sv_password ${PASSWORD} +sv_load_forced_client_names_file "names.txt" 

