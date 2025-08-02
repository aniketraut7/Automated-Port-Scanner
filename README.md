# 🔍 Automated Port Scanner

A fast and simple Python-based port scanner built using the `socket` module. Ideal for beginners and cybersecurity enthusiasts practicing reconnaissance techniques.

---

## ⚙️ Features

- 🔎 Scan specific IPs or domains
- 📍 Define custom port ranges
- ✅ Clean output with open ports
- 🧱 Pure Python — no external libraries

---


### 📥 Installation:
```bash
git clone https://github.com/YOUR_USERNAME/Automated-Port-Scanner.git
cd Automated-Port-Scanner
chmod +x setup.sh  # Make script executable
./setup.sh         # Run setup
source venv/bin/activate  # Activate environment
python scanner.py <target>  # Run scanner


🔍 Usage:
python scanner.py <target> -p <ports>

Example:
python scanner.py 192.168.1.1 -p 80,443,21

```
```
## 📸 Example Output

Enter the target IP or domain: 192.168.1.1
Enter the starting port: 20
Enter the ending port: 100

[+] Scanning 192.168.1.1 from port 20 to 100...

[+] Port 22 is open
[+] Port 80 is open

Scan completed in 0.76 seconds.
```
```
📝 Requirements
    Python 3.x
    nmap installed (apt install nmap for Linux)
    

📩 Contact
🔗 GitHub: @aniketraut7
✉️ Email: aniketsraut7@gmail.com
```
