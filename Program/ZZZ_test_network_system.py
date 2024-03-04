import threading
import time
from CLIENT_Client_Info import Client_Info
from UTILS_networking import get_private_ip
# Assuming RegistrationServer and RegistrationClient are available for import
from SERVER_RegistrationServer import RegistrationServer
from CLIENT_RegistrationClient import RegistrationClient

def start_server():
    server = RegistrationServer()
    server.start_server()

def test_client_server_operations_local():
    # Allow the server some time to start up
    time.sleep(1)

    # Initialize the client
    server_host = '127.0.0.1'
    server_port = 9999
    
    # Example client ID and information
    client_info = Client_Info("client123", get_private_ip(), "5050")
    
    # client = RegistrationClient(server_host, server_port)
    
    # Register this client with the server
    # print("Registering client...")
    # client.register_with_server(client_id, client_info)
    
    # Request information for the same client
    # print("Requesting client info...")
    # client.request_client_info(client_id)

if __name__ == "__main__":
    # Start the server in a background thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # Run client operations for testing
    test_client_server_operations_local()