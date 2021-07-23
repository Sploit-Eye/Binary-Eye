#!/bin/bash
# Run this file first to avoid errors in main.py
# This script will install all required tools for main.py
clear
tput setaf 2; echo """
█▀█ █▀▀ █▀█ █░█ █ █▀█ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀
█▀▄ ██▄ ▀▀█ █▄█ █ █▀▄ ██▄ █░▀░█ ██▄ █░▀█ ░█░ ▄█
"""
tput sgr0;
echo ""
sleep 1.5
echo "- Checking required tools..."
sudo apt install python3 -y # Installing Python3
sudo apt install ncurses-utils -y # Installing Ncurses-utils for output colors
clear
tput setaf 2;
python3 --version # Check Python version
sleep 1.4
tput -V # Check Ncurses-utils version
sleep 1.4
tput sgr0;
clear
echo "- Required tools are installed."
sleep 1.1
echo "- Running Binary Eye..."
sleep 0.4
echo "- Script is running..."
sleep 0.6
clear
sleep 1
python3 main.py # Runs python script [Binary-Eye]
