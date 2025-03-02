import nmap
import argparse
import sys
import pyfiglet
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

# Scan function
def scan_target(target, ports):
    console.print(f"\n🔎 Scanning [bold yellow]{target}[/bold yellow] on ports {ports}...\n", style="bold green")

    # Progress Bar Simulation
    for _ in track(range(10), description="Scanning..."):
        sleep(0.3)

    # Check if Nmap is installed
    try:
        nm = nmap.PortScanner()
    except nmap.nmap.PortScannerError:
        console.print("[red]❌ Nmap is not installed! Install it and try again.[/red]", style="bold red")
        sys.exit(1)
    
    try:
        nm.scan(target, ports)
        if target not in nm.all_hosts():
            console.print(f"[red]❌ Error:[/red] Unable to scan {target}. It may be down or blocking scans.", style="bold red")
            sys.exit(1)

        for port in nm[target]['tcp']:
            state = nm[target]['tcp'][port]['state']
            console.print(f"🔹 Port {port}: {state.upper()}", style="bold blue")

    except Exception as e:
        console.print(f"[red]❌ Error:[/red] {str(e)}", style="bold red")

def main():
    print_banner()  # ✅ Keep only this call
    
    parser = argparse.ArgumentParser(description="Auto_Scanner - A Kali Linux Vulnerability Scanner")
    parser.add_argument("target", help="Target IP or Domain")
    parser.add_argument("-p", "--ports", default="1-1000", help="Port range to scan (default: 1-1000)")

    args = parser.parse_args()
    scan_target(args.target, args.ports)

if __name__ == "__main__":
    main()
