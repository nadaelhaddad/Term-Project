import subprocess
import sys

def throughput_test(target_ip, port='5201'):
    try:
        subprocess.run(['iperf3', '-c', target_ip, '-p', port], check=True)
        print(f"Throughput test to {target_ip} on port {port} was successful.")
    except subprocess.CalledProcessError:
        print(f"Throughput test to {target_ip} on port {port} failed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 throughput_test.py <target_ip>")
        sys.exit(1)
    ip = sys.argv[1]
    throughput_test(ip)
