import socket

from UTILS_networking import get_private_ip, get_free_port, setup_port_forward
from UTILS_networking import get_public_ip
from CLIENT_Client_Info import Client_Info

from PROTOCOL_Request import RequestBody, RequestHeader, RequestTypes, Request
from PROTOCOL_Response import Response, ResponseBody, ResponseHeader, ResponseTypes
from SERVER_RegistrationServer import RegistrationServer
from connectivity_test import connectivity_test

class RegistrationClient:
    def __init__(self, server_host: str, server_port: int, client_info: Client_Info):
        self.server_host = server_host
        self.server_port = server_port
        self.client_info = client_info
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def register_with_server(self, client_info):
        """Register this client with the registration server."""
        #Serialize client info and send to server
        requestHeader = RequestHeader(RequestTypes.REGISTER)
        requestBody = RequestBody(client_info.serialize())
        request = Request(requestHeader, requestBody)
         
        self.sock.connect((self.server_host, self.server_port))
        self.sock.sendall(request.encode_and_serialize())
        response = Response.decode_and_desearialize(self.sock.recv(1024))
        self.sock.close()
        return response.header.type

    
    def request_client_info(self, client_id):
        """Request information for a specific client by ID."""
        requestHeader = RequestHeader(RequestTypes.RETRIEVE)
        requestBody = RequestBody(client_id)
        request = Request(requestHeader,requestBody)

        self.sock.connect((self.server_host, self.server_port))
        self.sock.sendall(request.encode_and_serialize())
        response = Response.decode_and_desearialize(self.sock.recv(1024))
        self.sock.close()
        return response.body.data

        
    def request_all_clients(self):
        """Request the details of all the clients registered at the server."""
        requestHeader = RequestHeader(RequestTypes.RETRIEVEALL)
        requestBody = RequestBody()
        request = Request(requestHeader, requestBody)
         
        self.sock.connect((self.server_host, self.server_port))
        self.sock.sendall(request.encode_and_serialize())
        response = Response.decode_and_desearialize(self.sock.recv(1024))    
        self.sock.close()
        return response.body.data

        

    def deregister_with_server(self, client_id):
        """Degesisters this client from this server"""
        requestHeader = RequestHeader(RequestTypes.DEREGISTER)
        requestBody = RequestBody(client_id)
        request = Request(requestHeader,requestBody)

        self.sock.connect((self.server_host, self.server_port))
        self.sock.sendall(request.encode_and_serialize())
        response = Response.decode_and_desearialize(self.sock.recv(1024))    
        self.sock.close()
        return response.body.data




if __name__ == "__main__":
    # LOCAL TEST
    server_host = '127.0.0.1'
    server_port = 9999
    client_nickname = "Amna"
    client_private_ip =  get_private_ip()
    client_listening_port = "5050"
    
    client_info = Client_Info(client_nickname, client_private_ip, client_listening_port)
    client = RegistrationClient(server_host, server_port, client_info)

    # Register this client with the server
    client.register_with_server(client_info)

    # Request information for a specific client (can be this client or another)
    client.request_client_info(client_nickname)
    
    # Request information for all clients on server
    client.request_all_clients()

    client.deregister_with_server(client_nickname)
    
    #Run connectivity test on specific client
    target_ip = "10.30.13.53"
    target_port = get_free_port()
    

    # connectivity_test(target_ip,target_port)

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
    
    
