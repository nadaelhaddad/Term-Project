import subprocess
import sys

def connectivity_test(target_ip, target_port):
    try:
        # The '-z' flag tells Netcat to scan without sending any data
        # The '-v' flag enables verbose mode to get more information
        result = subprocess.run(['nc', '-zv', target_ip, str(target_port)], 
                                capture_output=True, text=True, check=True)
        print(f"Success! Port {target_port} on {target_ip} is open.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to port {target_port} on {target_ip}.")
        print(e.stderr)

if __name__ == "__main__":
    # if len(sys.argv) != 3:
    #     print("Usage: python3 connectivity_test.py <target_ip> <target_port>")
    #     sys.exit(1)
    target_ip = "127.0.0.1"
    target_port = 9999
    connectivity_test(target_ip, target_port)
