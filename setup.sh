#!/bin/bash
sys=$(lsb_release -si)
case $sys in
  ArchLinux|ManjaroLinux)
    pamac install netcat --no-confirm
    ;;
  *)
    apt-get install netcat --no-confirm
    ;;
esac
