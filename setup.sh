#!/usr/bin/bash
sys=$(lsb_release -si)
case $sys in
  ArchLinux|ManjaroLinux)
    sys='pamac'
    conf='--no-confirm'
    ;;
  *)
    sys='apt-get'
    conf='-y'
    ;;
esac
clear
"$sys" update "$conf" && "$sys" upgrade "$conf"
"$sys" install netcat "$conf"

