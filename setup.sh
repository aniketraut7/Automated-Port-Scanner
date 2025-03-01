#!/bin/bash

echo "Updating system and installing dependencies..."
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nmap

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment and installing requirements..."
source venv/bin/activate
pip install -r requirements.txt

echo "Setup complete! To activate the environment, run: source venv/bin/activate"
