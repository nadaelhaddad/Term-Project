import unittest
from unittest.mock import patch, MagicMock
from SERVER_RegistrationServer import RegistrationServer
from CLIENT_Client_Info import Client_Info
from PROTOCOL_Request import Request, RequestHeader, RequestBody, RequestTypes
from PROTOCOL_Response import ResponseTypes

class TestRegistrationServer(unittest.TestCase):
    def setUp(self):
        """Prepare test environment"""
        # Setup a temporary JSON file for testing
        self.temp_json_file = 'temp_test_clients.json'
        self.server = RegistrationServer(JSON_file=self.temp_json_file)

    def tearDown(self):
        """Clean up after tests"""
        # Remove the temporary JSON file if needed
        import os
        if os.path.exists(self.temp_json_file):
            os.remove(self.temp_json_file)


    # Replaces socket.socket objects with mock (or fake) objects
        # Any instances of socket.socket will be replaced with MagicMock objects.
    @patch('socket.socket') 
    def test_register_client(self, mock_socket):
        """Test client registration"""
        # Setup mock socket
        mock_socket_instance = MagicMock() # 
        mock_socket.return_value = mock_socket_instance
        
        # Prepare mocked socket response to simulate client registration request
        client_info = Client_Info("TestUser", "192.168.1.1", "5050")
        request = Request(RequestHeader(RequestTypes.REGISTER), RequestBody(client_info.serialize()))
        mock_socket_instance.recv.return_value = request.encode_and_serialize()

        # Start server in test mode (no need for threading or actual network listening)
        self.server.handle_client(mock_socket_instance)

        # Verify client was added
        data = self.server._load_data()
        try:
            self.assertIn("TestUser", data)
            print("TEST SUCCEEDED: TestUser is found in data file")
        except AssertionError as e:
            print("TEST FAILED: TestUser is not found in data file")
            raise e # Re-raise Exception

if __name__ == '__main__':
    unittest.main()