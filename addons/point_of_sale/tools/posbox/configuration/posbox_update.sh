#!/usr/bin/env bash

sudo mount -o remount,rw /
sudo git --work-tree=/home/pi/gerp/ --git-dir=/home/pi/gerp/.git pull
sudo mount -o remount,ro /
(sleep 5 && sudo reboot) &
