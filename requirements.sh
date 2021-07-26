#!/usr/bin/env bash
# Run this file first to avoid errors in main.py
# This script will install all required tools for main.py
clear
tput setaf 2; echo """
█▀█ █▀▀ █▀█ █░█ █ █▀█ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀
█▀▄ ██▄ ▀▀█ █▄█ █ █▀▄ ██▄ █░▀░█ ██▄ █░▀█ ░█░ ▄█
"""
tput sgr0;
echo "be-1.4-se"
echo ""
sleep 1.0
echo "- Checking required tools..."
sudo apt install python3 -y # Installing Python3
sudo apt install ncurses-utils -y # Installing Ncurses-utils for output colors
clear
tput setaf 2;
printf "-" && python3 --version # Check Python version
sleep 0.6
printf "-" && tput -V # Check Ncurses-utils version
sleep 0.6
tput sgr0;
clear
tput setaf 2;
echo "- Required tools are installed."
tput sgr0;
sleep 0.3
tput setaf 2;
echo "- Running Binary Eye..."
sleep 0.1
tput sgr0;
tput setaf 2;
echo "- Script is running..."
tput sgr0;
sleep 0.1
clear
sleep 1
python3 main.py # Runs python script [Binary-Eye]
