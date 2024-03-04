import socket

from UTILS_networking import get_private_ip, setup_port_forward
from UTILS_networking import get_public_ip
from CLIENT_Client_Info import Client_Info


class RegistrationClient:
    def __init__(self, server_host: str, server_port: int, client_info: Client_Info):
        self.server_host = server_host
        self.server_port = server_port
        self.client_info = client_info

    def register_with_server(self, client_info):
        """Register this client with the registration server."""
        pass
    
    def request_client_info(self, client_id):
        """Request information for a specific client by ID."""
        pass
        
    def request_all_clients(self, client_id):
        """Request the details of all the clients registered at the server."""
        pass
        

    def send_message_to_server(self, message):
        """Handles sending a message to the server and receiving the response."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.server_host, self.server_port))
            pass # sock.sendall(...)
            response = sock.recv(1024)
            return response




if __name__ == "__main__":
    # LOCAL TEST
    server_host = '127.0.0.1'
    server_port = 9999
    client_nickname = "Aakash"
    client_private_ip =  get_private_ip()
    client_listening_port = "5050"
    
    client_info = Client_Info(client_nickname, client_private_ip, client_listening_port)
    client = RegistrationClient(server_host, server_port, client_info)

    # Register this client with the server
    client.register_with_server(client_info)

    # Request information for a specific client (can be this client or another)
    client.request_client_info(client_nickname)
    
    
# if __name__ == "publicIP":
#     # PUBLIC IP TEST
#     server_host = '127.0.0.1'
#     server_port = 9999
#     client_nickname = "Aakash"
#     client_public_ip = get_public_ip()   # Get the public IP using an API service
#     client_listening_port = "5050"
#     setup_port_forward(client_listening_port)   # Tells the router to send requests received at the listening port to the client
    
#     client_info = Client_Info(client_nickname, client_public_ip, client_listening_port)
#     client = RegistrationClient(server_host, server_port, client_info)

#     # Register this client with the server
#     client.register_with_server(client_info)

#     # Request information for a specific client (can be this client or another)
#     client.request_client_info(client_nickname)
    
    
