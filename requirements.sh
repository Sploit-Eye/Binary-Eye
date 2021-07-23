#!/bin/bash
# Run this file first to avoid errors in main.py
# This script will install all required tools for main.py
clear
tput setaf 2; echo """
█▀█ █▀▀ █▀█ █░█ █ █▀█ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀
█▀▄ ██▄ ▀▀█ █▄█ █ █▀▄ ██▄ █░▀░█ ██▄ █░▀█ ░█░ ▄█
"""
echo "Version: be-1.2-se"
tput sgr0;
echo ""
sleep 1.5
echo "- Checking required tools..."
sudo apt install python3 -y # Installing Python3
sudo apt install ncurses-utils -y # Installing Ncurses-utils for output colors
clear
tput setaf 2;
printf "-" && python3 --version # Check Python version
sleep 1.4
printf "-" && tput -V # Check Ncurses-utils version
sleep 1.4
tput sgr0;
clear
tput setaf 1;
echo "- Required tools are installed."
tput sgr0;
sleep 1.1
tput setaf 1;
echo "- Running Binary Eye..."
sleep 0.4
tput sgr0;
tput setaf 2;
echo "- Script is running..."
tput sgr0;
sleep 0.6
clear
sleep 1
python3 main.py # Runs python script [Binary-Eye]
