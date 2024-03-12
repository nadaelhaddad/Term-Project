import unittest
from unittest.mock import patch
import threading
from SERVER_RegistrationServer import RegistrationServer
from CLIENT_Client_Info import Client_Info
from CLIENT_RegistrationClient import RegistrationClient
from PROTOCOL_Response import ResponseTypes 



class IntegrationTestClientServerRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up a server instance before tests"""
        cls.server = RegistrationServer('127.0.0.1', 9999, 'temp_test_clients_integration.json')
        cls.server_thread = threading.Thread(target=cls.server.start_server, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests"""
        import os
        cls.server_thread.join()
        if os.path.exists('temp_test_clients_integration.json'):
            os.remove('temp_test_clients_integration.json')

    def test_client_registration_flow(self):
        """Test the entire flow from registration to deregistration"""
        client_info = Client_Info("IntegrationTestUser", "127.0.0.1", "5050")
        client = RegistrationClient('127.0.0.1', 9999, client_info)

        # Test registration
        response = client.register_with_server(client_info)
        self.assertEqual(response.header.type, ResponseTypes.SUCCESS, "Client registration failed")

        # Test retrieve
        response = client.request_client_info("IntegrationTestUser")
        retrieved_info = response.body.data
        self.assertIsNotNone(retrieved_info, "Failed to retrieve registered client info")

        # Test retrieve all
        response = client.request_all_clients()
        all_clients_info = response.body.data
        self.assertIn("IntegrationTestUser", all_clients_info, "Failed to retrieve all clients info")

        # Test deregistration
        response = client.deregister_with_server("IntegrationTestUser")
        self.assertEqual(response.header.type, ResponseTypes.SUCCESS, "Client deregistration failed")

if __name__ == '__main__':
    unittest.main()