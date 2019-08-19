#!/bin/bash
#   startup.sh
#   Bash shell
#   Version 0.0.1
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
VERSION="0.2.2"
# Root checker
function am_i_root(){
	if [[ $EUID -ne 0 ]]; then
		echo " [!] No root permission detected [!]"
		echo " [i] To run this command, you should be root"
		echo ""
		exit
	fi
}
# Usage
function usage(){
	echo " [i] Usage: "
	echo "       --help              Display this page"
	echo "       --start             Start the bot"
	echo "       --update            Update bot"
  echo "       --init              Init bot enviroment"
	echo ""
}
# Name and intro of the Script
sleep 1
echo "[+] FelineSec Telegram bot [+]"
echo "Startup coded by Francesco Masala (https://github.com/francescomasala)"
sleep 1
if [ -z "$1" ]; then
	echo " [!] No argument supplied. [!]"
	usage
	exit 1
elif [ "$1" = "--help" ]; then
	usage
	exit 0
elif [ "$1" = "--version" ]; then
	echo "Version $VERSION"
	echo ""
	exit 0
elif [ "$1" = "--start" ]; then
	echo "[+] FelineSec Telegram bot [+]"
	am_i_root
	echo "[!] Using root access [!]"
  sudo python3 main.py
elif [ "$1" = "--update" ]; then
	git pull
	exit 0
elif [ "$1" = "--init" ]; then
  am_i_root
	echo "[!] Using root access [!]"
	sudo pip3 install -r requirements.txt
	exit 0
fi
