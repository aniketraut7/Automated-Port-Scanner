#!/bin/bash

echo "🚀 Setting up Auto_Scanner on Kali Linux..."

# Step 1: Update the system
echo "[+] Updating system packages..."
sudo apt update -y && sudo apt upgrade -y

# Step 2: Install required dependencies
echo "[+] Installing Python and required dependencies..."
sudo apt install python3 python3-pip python3-venv nmap -y

# Step 3: Create a virtual environment
echo "[+] Creating a virtual environment..."
python3 -m venv venv

# Step 4: Activate the virtual environment
echo "[+] Activating the virtual environment..."
source venv/bin/activate

# Step 5: Install Python dependencies
echo "[+] Installing necessary Python libraries..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 6: Verify Installation
echo "[+] Verifying installation..."
python3 -m pip list

echo "✅ Setup complete! You can now run the scanner with:"
echo "   source venv/bin/activate"
echo "   python scanner.py <target>"
