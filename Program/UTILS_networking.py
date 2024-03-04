# import miniupnpc
def setup_port_forward(port) -> bool:
    # upnp = UPnP()
    # upnp.discoverdelay = 200
    # upnp.discover()
    # upnp.selectigd()
    # # Attempt to add a port mapping
    # result = upnp.addportmapping(port, 'TCP', upnp.lanaddr, port, 'CN Registration Application', '')
    # if result:
    #     print("Port forwarding successfully set up.")
    # else:
    #     print("Failed to set up port forwarding. Check if UPnP is enabled on your router.")
    
    # return result
    
    return True # Placeholder for port-forwarding script.


import socket
def get_private_ip() -> str:
    # Attempt to connect to an external address (does not need to succeed)
    try:
        # Use a dummy socket to connect to a public DNS server (e.g., Google's)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            # Get the socket's own address
            private_ip = s.getsockname()[0]
            return private_ip
    except Exception as e:
        print(f"Error obtaining private IP address: {e}")
        return ""

import requests
def get_public_ip() -> str:
    # Using a public IP address API service
    response = requests.get('https://api.ipify.org')
    return response.text