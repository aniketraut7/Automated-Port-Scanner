import argparse
import nmap
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.progress import Progress

# Initialize rich console
console = Console()

# Banner function
def print_banner():
    banner = Text("""
    █████╗ ██╗   ██╗ ██████╗ ███████╗██╗      ██████╗ ██╗   ██╗
   ██╔══██╗██║   ██║██╔════╝ ██╔════╝██║     ██╔═══██╗██║   ██║
   ███████║██║   ██║██║  ███╗█████╗  ██║     ██║   ██║██║   ██║
   ██╔══██║██║   ██║██║   ██║██╔══╝  ██║     ██║   ██║██║   ██║
   ██║  ██║╚██████╔╝╚██████╔╝███████╗███████╗╚██████╔╝╚██████╔╝
   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝ ╚═════╝  ╚═════╝
    """, style="bold red")
    console.print(banner)
    console.print("[bold cyan]🔍 Automated Vulnerability Scanner - Kali Linux Edition[/bold cyan]")

# Perform a basic port scan
def scan_target(target, ports):
    nm = nmap.PortScanner()

    console.print(f"\n[bold yellow]🔎 Scanning {target} on ports {ports}...[/bold yellow]\n")

    with Progress() as progress:
        task = progress.add_task("[cyan]Scanning...", total=100)
        for _ in range(10):
            progress.update(task, advance=10)

    nm.scan(target, ports)
    
    table = Table(title=f"Scan Results for {target}", show_header=True, header_style="bold magenta")
    table.add_column("Port", justify="right", style="cyan")
    table.add_column("State", justify="center", style="green")
    table.add_column("Service", justify="left", style="yellow")

    for port in nm[target]['tcp']:
        state = nm[target]['tcp'][port]['state']
        service = nm[target]['tcp'][port]['name']
        table.add_row(str(port), state, service)

    console.print(table)

# CLI argument handling
def main():
    print_banner()

    parser = argparse.ArgumentParser(description="Automated Vulnerability Scanner - Kali Edition")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-p", "--ports", default="1-1000", help="Port range to scan (default: 1-1000)")

    args = parser.parse_args()
    scan_target(args.target, args.ports)

if __name__ == "__main__":
    main()
