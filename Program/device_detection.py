
import nmap
import sys

def scan_network(subnet):
    nm = nmap.PortScanner()
    nm.scan(hosts=subnet, arguments='-sn')  # -sn for ping scan
    for host in nm.all_hosts():
        if nm[host].state() == "up":
            print(f"Host {host} is up")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 device_detection.py <subnet>")
        sys.exit(1)
    subnet = sys.argv[1]
    scan_network(subnet)
