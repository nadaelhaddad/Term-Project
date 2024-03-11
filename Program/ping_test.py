import subprocess
import sys

def ping_test(destination_ip):
    try:
        subprocess.run(['ping', '-c', '4', destination_ip], check=True)
        print(f"Ping to {destination_ip} successful.")
    except subprocess.CalledProcessError:
        print(f"Failed to ping {destination_ip}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ping_test.py <destination_ip>")
        sys.exit(1)
    ip = sys.argv[1]
    ping_test(ip)
