#!/usr/bin/env python3

import socket
import argparse
import time

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is open")
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple Automated Port Scanner by Lucifer")
    parser.add_argument("-t", "--target", help="Target IP or domain", required=True)
    parser.add_argument("-s", "--start", type=int, help="Start port", required=True)
    parser.add_argument("-e", "--end", type=int, help="End port", required=True)

    args = parser.parse_args()

    target = args.target
    start_port = args.start
    end_port = args.end

    # Validate port range
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("[-] Invalid port range. Ports must be between 1 and 65535 and start < end.")
        return

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[-] Unable to resolve hostname. Please check the target.")
        return

    print(f"\n[+] Scanning {ip} from port {start_port} to {end_port}...\n")
    start_time = time.time()

    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    print(f"\n[✔] Scan completed in {total_time} seconds.")

if __name__ == "__main__":
    main()
