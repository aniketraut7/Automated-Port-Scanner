#!/bin/bash

echo "🚀 Setting up Auto_Scanner on Kali Linux..."

# Step 1: Install required dependencies
echo "[+] Installing Python and required dependencies..."
sudo apt install python3 python3-pip python3-venv nmap -y

# Step 2: Create a virtual environment
echo "[+] Creating a virtual environment..."
python3 -m venv venv

# Step 3: Activate the virtual environment
echo "[+] Activating the virtual environment..."
source venv/bin/activate

pip install -r requirements.txt

# Step 4: Install Python dependencies
echo "[+] Installing necessary Python libraries..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 5: Verify Installation
echo "[+] Verifying installation..."
python3 -m pip list

echo "✅ Setup complete! You can now run the scanner with:"
echo "   source venv/bin/activate"
echo "   python scanner.py <target>"
