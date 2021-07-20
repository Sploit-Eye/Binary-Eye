#!/bin/bash
# Run this file first to avoid errors in main.py
# This script will install all required tools for main.py
clear
echo """
█▀█ █▀▀ █▀█ █░█ █ █▀█ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀
█▀▄ ██▄ ▀▀█ █▄█ █ █▀▄ ██▄ █░▀░█ ██▄ █░▀█ ░█░ ▄█
"""
echo ""
sleep 2
echo "- Checking required tools..."
sudo apt install python3 -y # Installing Python3
clear
python3 --version # Check Python version
sleep 3
clear
echo ""
clear
echo "- Required tools are installed."
sleep 1.9
clear
echo "- Running Text-to-Binary..."
sleep 2.1
clear
echo "- Launched"
sleep 2.3
python3 main.py # Runs python script [text-to-binary]
exit 1
