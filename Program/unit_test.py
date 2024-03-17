# unit_test
import unittest
from unittest.mock import patch
from io import StringIO
import sys


from ping_test import ping_test
from throughput_test import throughput_test
from connectivity_test import connectivity_test
from scan_network import scan_network

class TestNetworkMethods(unittest.TestCase):

    @patch('ping_test.subprocess.run')
    def test_ping_test(self, mock_run):
        mock_run.return_value.returncode = 0  # Simulate success
        capturedOutput = StringIO()         
        sys.stdout = capturedOutput                   
        ping_test('10.30.4.79')                     
        sys.stdout = sys.__stdout__                   
        self.assertIn("Ping to 10.30.4.79 successful", capturedOutput.getvalue())

    @patch('throughput_test.subprocess.run')
    def test_throughput_test(self, mock_run):
        mock_run.return_value.returncode = 0  # Simulate success
        capturedOutput = StringIO()         
        sys.stdout = capturedOutput                   
        throughput_test('10.30.4.79')                  
        sys.stdout = sys.__stdout__                   
        self.assertIn("Throughput test to 10.30.4.79 on port 5201 was successful", capturedOutput.getvalue())

    @patch('connectivity_test.subprocess.run')
    def test_connectivity_test(self, mock_run):
        mock_run.return_value.returncode = 0  # Simulate success
        capturedOutput = StringIO()         
        sys.stdout = capturedOutput                   
        connectivity_test('10.30.4.79', '22')          
        sys.stdout = sys.__stdout__                   
        self.assertIn("Success! Port 22 on 10.30.4.79 is open", capturedOutput.getvalue())

    @patch('scan_network.nmap.PortScanner')
    def test_scan_network_detection(self, mock_scan):
        # Create a mock PortScanner object
        mock_scanner = mock_scan.return_value
        # Simulate the scan method
        mock_scanner.scan.return_value = {}
        # Simulate the all_hosts method to return a list of hosts
        mock_scanner.all_hosts.return_value = ['10.30.4.79']
        # Ensure the state method returns "up" for the mock host
        mock_scanner.__getitem__.return_value.state.return_value = "up"

        capturedOutput = StringIO()
        original_stdout = sys.stdout
        try:
            sys.stdout = capturedOutput
            # Call the function under test
            scan_network('10.30.4.0/24')
        finally:
            # Restore stdout
            sys.stdout = original_stdout

        # Check if the expected string is in the captured output
        self.assertIn("Host 10.30.4.79 is up", capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main(verbosity=2)
