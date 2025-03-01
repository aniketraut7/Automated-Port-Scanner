import nmap
import shodan

# Set your Shodan API key here
SHODAN_API_KEY = "UeXxptNxjyKXZGHh9bGhM7PnqF5XpNLn"

def scan_ports(target):
    """Scan open ports using Nmap"""
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments="-sV")  # Scans for open ports & versions

    open_ports = {}
    for host in scanner.all_hosts():
        for port, details in scanner[host]['tcp'].items():
            open_ports[port] = details['name']
    
    return open_ports

def check_vulnerabilities(port, service):
    """Check for vulnerabilities using Shodan API"""
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        results = api.search(service)
        for result in results['matches'][:5]:  # Limit results for readability
            print(f"⚠️ Possible Vulnerability Found: {result['ip_str']} - {result['hostnames']}")
    except shodan.APIError as e:
        print(f"Shodan API Error: {e}")

def main():
    target = input("Enter target IP/Domain: ")
    print("\n🔍 Scanning for open ports...\n")

    open_ports = scan_ports(target)
    
    if not open_ports:
        print("❌ No open ports found.")
        return

    print(f"✅ Found Open Ports: {open_ports}")

    for port, service in open_ports.items():
        print(f"\n🔎 Checking vulnerabilities for {service} on port {port}...")
        check_vulnerabilities(port, service)

if __name__ == "__main__":
    main()
