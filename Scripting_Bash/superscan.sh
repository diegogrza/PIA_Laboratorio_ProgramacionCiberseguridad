#!/bin/bash
#Diego Garza Martinez
#29/09/2022
# Ejemplo de Menu en BASH
#
date
    echo "---------------------------"
    echo "     Menu Principal"
    echo "                      "
    echo "─────█─▄▀█──█▀▄─█─────"
    echo "────▐▌──────────▐▌────"
    echo "────█▌▀▄──▄▄──▄▀▐█────"
    echo "───▐██──▀▀──▀▀──██▌───"
    echo "──▄████▄──▐▌──▄████▄──"

    echo "---------------------------"
    echo "1. Net Discover"
    echo "2. PortScan"
    echo "3. Welcome"
    echo "4. Exit"
read -p "Opción  [ 1 - 4 ] " c
case $c in
        1) $HOME/practica06/netdiscover.sh;;
        2) $HOME/practica06/portscan1.sh;;
        3) $HOME/practica06/welcome.sh;;
        4) echo "Bye!"; exit 0;;
esac
