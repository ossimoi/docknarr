#!/bin/bash
for x in $(docker ps | awk ' { print $1 } '); do docker kill $x; done
for x in $(docker ps -a | awk ' { print $1 } '); do docker rm $x; done
for i in $(ovs-vsctl show |grep -i error | awk '{ print $7 }'); do ovs-vsctl del-port $i; done

