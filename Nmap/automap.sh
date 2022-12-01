#!/bin/bash

#Diego Garza Martinez

#20/10/2022

# Ejemplo de Menu en BASH

#

    echo "---------------------------"

    echo "     Menu Principal"

    echo "                      "

    echo "─────█─▄▀█──█▀▄─█─────"

    echo "────▐▌──────────▐▌────"

    echo "────█▌▀▄──▄▄──▄▀▐█────"

    echo "───▐██──▀▀──▀▀──██▌───"

    echo "──▄████▄──▐▌──▄████▄──"



    echo "---------------------------"

    echo "1. Escaneo de subred"

    echo "2. Escaneo individual"

    echo "3. Escaneo UDP"

    echo "4. Escaneo de script"

    echo "5. Salir"

read -p "Opción  [ 1 - 5 ] " c



case $c in

	1)

		echo "Bienvenido al escaneo de subred, se guardara la info en el archivo scan_subred.txt"

		read -p "Ingresa el ip de la subred : " ip

		sudo nmap -sn $ip -oN scan_subred.txt

	;;

	2)

		echo "Bienvenido al escaneo individual, se guardara la info en el archivo scan_individual.txt"

		read -p "Ingresa el ip para el scan : " ip

		sudo nmap -v -A $ip -oN scan_individual.txt

	;;

	3)

		echo "Bienvenido al escaneo UDP , se guardara la info en scan_udp.txt"

		read -p "Ingresa el ip para el scan UDP : " ip

		sudo nmap -sU $ip -oN scan_udp.txt

	;;

	4)

		echo "Bienvenido al escaneo de script, se guardara la info en scan_script.txt"

		read -p "Ingresa el ip para el scan : " ip

		read -p "Ingresa el nombre del script : " script

		sudo nmap --script $script $ip -oN scan_script.txt

	;;

	5)

		echo "Adios!"

		echo "───▄▄▄"

		echo "─▄▀░▄░▀▄"

		echo "─█░█▄▀░█"

		echo "─█░▀▄▄▀█▄█▄▀"

		echo "▄▄█▄▄▄▄███▀"



esac