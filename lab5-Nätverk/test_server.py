import subprocess
import netifaces as ni

class TestServer:
    ROUTER_IP = '10.0.0.1'
    CLIENT_1_IP = '10.0.0.2'
    CLIENT_2_IP = '10.0.0.3'
    MY_IP = '10.0.0.4'
    MY_INTERFACE = 'ens3'
    NETMASK = '255.255.255.0'

    def test_my_ip(self):
        ip = ni.ifaddresses(self.MY_INTERFACE)[ni.AF_INET][0]['addr']
        assert ip == self.MY_IP

    def test_my_netmask(self):
        netmask = ni.ifaddresses(self.MY_INTERFACE)[ni.AF_INET][0]['netmask']
        assert netmask == self.NETMASK

    def test_ping_google(self):
        response = subprocess.run(['ping', 'google.com', '-c 4'])
        assert response.returncode == 0
            
    def test_ping_router(self):
        response = subprocess.run(['ping', self.ROUTER_IP, '-c 4'])
        assert response.returncode == 0

    def test_ping_client_1(self):
        response = subprocess.run(['ping', self.CLIENT_1_IP, '-c 4'])
        assert response.returncode == 0
    
    def test_ping_client_2(self):
        response = subprocess.run(['ping', self.CLIENT_2_IP, '-c 4'])
        assert response.returncode == 0