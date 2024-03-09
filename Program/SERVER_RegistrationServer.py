import json
import socket
import threading
import os

from PROTOCOL_Request import Request, RequestTypes
from PROTOCOL_Response import Response, ResponseHeader, ResponseBody, ResponseTypes
from CLIENT_Client_Info import Client_Info
from UTILS_networking import get_public_ip, setup_port_forward

class RegistrationServer:
    def __init__(self, host='0.0.0.0', port=9999, JSON_file='clients.json'):
        self.host = host
        self.port = port
        self.JSON_file = JSON_file
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Create an empty JSON file if it doesn't already exist
        if not os.path.exists(self.JSON_file):
            with open(self.JSON_file, 'w') as file:
                json.dump({}, file)  # Initializes the file with an empty dictionary

    def start_server(self):
        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            client_socket, address = self.server.accept()
            print(f"Accepted connection from {address[0]}:{address[1]}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket: socket.socket):
        responseHeader = ResponseHeader()
        responseBody = ResponseBody()
        
        try:
            # Expecting data in the format: "REGISTER:<client_info>" DEREGISTER:<Nickname>:<client_info>" or "RETRIEVE:Nickname" or "RETRIEVEALL"                            
            request = Request.decode_and_desearialize(client_socket.recv(1024))
            
            # REGISTER returns an assigned client_id.
            if request.header.type == RequestTypes.REGISTER:
                client_info = Client_Info.deserialize(request.body.data)
                self.register_client(client_info.get_nickname(), client_info)
                responseHeader = ResponseHeader(ResponseTypes.SUCCESS)
                responseBody = ResponseBody(f"Nickname {client_info.get_nickname} registered")
            
            # DEREGISTER returns a response along with the removed client_id.
            elif request.header.type == RequestTypes.DEREGISTER:
                nickname = request.body.data
                if (self.deregister_client(nickname)):
                    responseHeader = ResponseHeader(ResponseTypes.SUCCESS)
                    responseBody = ResponseBody(f"Nickname {nickname} deregistered")
                    
                else:
                    responseHeader = ResponseHeader(ResponseTypes.BAD_REQUEST)
                    responseBody = ResponseBody(f"Nickname {nickname} not registered")
            
            # RETRIEVE returns the client_info of the found client if stored.
            elif request.header.type == RequestTypes.RETRIEVE:
                nickname = request.body.data
                client_info = self.retrieve(nickname)
                if (client_info != None):
                    responseHeader = ResponseHeader(ResponseTypes.SUCCESS)
                    responseBody = ResponseBody(f"{client_info.serialize()}")
                
                else:
                    responseHeader = ResponseHeader(ResponseTypes.BAD_REQUEST)
                    responseBody = ResponseBody(f"Nickname {nickname} not registered")
            
            # RETRIEVEALL returns a list of all the client_info stored.
            elif request.header.type == RequestTypes.RETRIEVEALL:
                nickname = request.body.data
                clients_list = self.retrieve_all()
                responseHeader = ResponseHeader(ResponseTypes.SUCCESS)
                responseBody = ResponseBody(f"{[client.serialize() for client in clients_list]}")
                            
        except Exception as e:
            responseHeader = ResponseHeader(ResponseTypes.SERVER_ERROR)
            responseBody = ResponseBody(str(e))
        
        finally:
            response = Response(responseHeader, responseBody)
            client_socket.sendall(response.encode_and_serialize())
            client_socket.close()


        # JSON File Format Expected to be the following:
            # {
            #   Nickname: {
            #       Nickname: "",
            #       IP: "", 
            #       ...
            #   },
            #   Nickname: {
            #       Nickname: "",
            #       IP: "", 
            #       ...
            #   },
            # }
    
    # JSON Methods        
    
    def _load_data(self):
        """Load All the Data from the JSON Document"""
        try:
            with open(self.JSON_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _save_data(self, data):
        """Save Data to JSON Document"""
        with open(self.JSON_file, 'w') as file:
            json.dump(data, file, indent=4)
    
    def _clear_data(self):
        """Clear All the Data from the JSON Document"""
        self._save_data({})
        
        
        
    def register_client(self, Nickname: str, client_info: Client_Info) -> bool:
        """Add client to JSON file"""
        data = self._load_data()
        if Nickname in data:
            print(f"Nickname {Nickname} already registered")
            raise Exception(f"Nickname {Nickname} already registered")

        data[Nickname] = client_info.serialize()
        self._save_data(data)
        
        return True
        

        
    def retrieve(self, Nickname: str) -> Client_Info | None:
        """Retrieve single client from JSON file based on a specified attribute"""
        data = self._load_data()
        return Client_Info.deserialize(data[Nickname]) if Nickname in data else None

        
        
    def retrieve_all(self) -> list[Client_Info]:
        """Retrieve all clients from JSON file"""
        data = self._load_data()
        return [Client_Info.deserialize(client_data) for client_data in data.values()]

        
        
    def deregister_client(self, Nickname: str) -> bool:
        """Remove specific client from JSON file"""
        data = self._load_data()
        if Nickname in data:
            del data[Nickname]
            self._save_data(data)
            return True
        
        return False        
    
    
if __name__ == "__main__":
#     # LOCAL IP
    server = RegistrationServer('127.0.0.1', 9999)
    server.start_server()
    
if __name__ == "publicIP":
    # PUBLIC IP
    server_host = get_public_ip()
    server_port = 9999
    server = RegistrationServer('127.0.0.1', 9999)
    setup_port_forward(9999)
    server.start_server()