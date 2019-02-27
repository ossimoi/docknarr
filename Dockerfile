FROM ubuntu:16.04
LABEL maintainer="ponky@pon.ky"

ARG CFGDIR=csgo

ENV USER csgo
ENV HOME /home/$USER
ENV STEAMCMD $HOME/steamcmd
ENV SERVER $HOME/csgoserver

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get -y install lib32gcc1 curl net-tools lib32stdc++6 \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && useradd $USER \
    && mkdir $HOME \
    && mkdir $STEAMCMD \
    && mkdir $SERVER \
    && chown $USER:$USER $HOME

RUN curl http://media.steampowered.com/client/steamcmd_linux.tar.gz | tar -C $STEAMCMD -xvz \
    && $STEAMCMD/steamcmd.sh +login anonymous +force_install_dir $SERVER +app_update 740 validate +quit

COPY cfg/$CFGDIR
COPY cfg/run.sh $HOME/run.sh

WORKDIR $SERVER
CMD /home/csgo/run.sh
