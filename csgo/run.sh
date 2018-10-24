#!/bin/bash
/home/csgo/csgoserver/srcds_run -console -usercon +game_type 0 +game_mode 1 +mapgroup mg_active +map de_cache -tickrate 128 +sv_setsteamaccount ${GSLT} +rcon_password ${RCONPW} -ip ${IP} +sv_password kingkong1 +sv_load_forced_client_names_file "server_player_names_csgo.txt" 

