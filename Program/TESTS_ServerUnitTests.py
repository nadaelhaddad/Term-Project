import os
import socket
import json
import sys
import threading
from typing import Optional


from CLIENT_Client_Info import Client_Info
from PROTOCOL_Request import RequestBody, RequestHeader, RequestTypes, Request
from PROTOCOL_Response import Response, ResponseBody, ResponseHeader, ResponseTypes
from SERVER_RegistrationServer import RegistrationServer

def create_server(host="127.0.0.1", port=9999, JSON_file="tests.json") -> RegistrationServer:
    return RegistrationServer(host, port, JSON_file)

def start_server(registrationServer: Optional[RegistrationServer] = None):
    # Create server if none are provided
    if registrationServer is None:
        registrationServer = create_server()
    
    # Start the server in a background thread
    server_thread = threading.Thread(target=registrationServer.start_server, daemon=True)
    server_thread.start()

    # Return True to indicate successful execution
    return True


def send_request_to_server():
    # Server details
    server_host = '127.0.0.1'
    server_port = 9999

    # Connect to the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((server_host, server_port))

    # Craft a REGISTER request
    client_nickname = "TestUser"
    client_public_ip = "192.168.1.1"
    client_listening_port = "5050"
    client_info = Client_Info(client_nickname, client_public_ip, client_listening_port)

    requestHeader = RequestHeader(RequestTypes.REGISTER)
    requestBody = RequestBody(client_info.serialize())
    request = Request(requestHeader, requestBody)
    
    # Send the request
    server_socket.sendall(request.encode_and_serialize())

    # Receive the response
    response = Response.decode_and_desearialize(server_socket.recv(1024))
    print("Response from server:", response.header.type)
    print("Message by server:", response.body.data)

    # Verify the response (this part is up to how you define success in your test)
    # For example, checking if the response contains a success message
    if response.header.type == ResponseTypes.SUCCESS:
        print("Test passed: Registration successful")
    else:
        print("Test failed: Unexpected server response")

    # Close the connection
    server_socket.close()
    

# start_server()
send_request_to_server()