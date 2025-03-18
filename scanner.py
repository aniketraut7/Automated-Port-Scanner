import nmap
import argparse
import sys
import pyfiglet
import socket
from time import sleep
from rich.console import Console
from rich.progress import track

console = Console()

def print_banner():
    banner_text = pyfiglet.figlet_format("Auto_Scanner")  # Generate ASCII text
    banner = f"""
{banner_text}
🔍 Auto_Scanner - Kali Linux Edition
"""
    console.print(banner, style="bold cyan")

def resolve_target(target):
    try:
        ip_address = socket.gethostbyname(target)
        console.print(f"✅ Resolved [bold yellow]{target}[/bold yellow] to [bold green]{ip_address}[/bold green]\n", style="bold green")
        return ip_address
    except socket.gaierror:
        console.print(f"[red]❌ Error:[/red] Could not resolve {target}. Check the domain name or internet connection.", style="bold red")
        sys.exit(1)

# Scan function
def scan_target(target, ports):
    console.print(f"\n🔎 Scanning [bold yellow]{target}[/bold yellow] on ports {ports}...\n", style="bold green")

    # Progress Bar Simulation (optional UX)
    for _ in track(range(10), description="Scanning..."):
        sleep(0.1)

    # Check if Nmap is installed
    try:
        nm = nmap.PortScanner()
    except nmap.PortScannerError:
        console.print("[red]❌ Nmap is not installed! Install it and try again.[/red]", style="bold red")
        sys.exit(1)

    # Perform the scan with error handling
    try:
        # Scan with default arguments; you can add '-Pn' to skip host discovery
        nm.scan(target, ports, arguments='-sS')

        if target not in nm.all_hosts():
            console.print(f"[red]❌ Error:[/red] Unable to scan {target}. It may be down, blocking scans, or invalid.", style="bold red")
            sys.exit(1)

        console.print(f"✅ Scan complete for [bold yellow]{target}[/bold yellow]!\n", style="bold green")
        
        for proto in nm[target].all_protocols():
            lport = nm[target][proto].keys()
            for port in sorted(lport):
                state = nm[target][proto][port]['state']
                console.print(f"🔹 Port {port}/{proto.upper()}: {state.upper()}", style="bold blue")

    except Exception as e:
        console.print(f"[red]❌ Error:[/red] {str(e)}", style="bold red")

def main():
    print_banner()  # Banner display
    
    parser = argparse.ArgumentParser(description="Auto_Scanner - A Kali Linux Vulnerability Scanner")
    parser.add_argument("target", help="Target IP or Domain")
    parser.add_argument("-p", "--ports", default="1-1000", help="Port range to scan (default: 1-1000)")

    args = parser.parse_args()

    # Resolve domain name to IP first (optional but good practice)
    resolved_target = resolve_target(args.target)
    
    scan_target(resolved_target, args.ports)

if __name__ == "__main__":
    main()
