import subprocess
import netifaces as ni

class TestDNSRouter:
    MY_IP = '10.0.0.2'
    ROUTER_IP = '10.0.0.2'
    CLIENT_2_IP = '10.0.0.3'
    NAME_SERVER_IP = '10.0.0.4'
    MY_INTERFACE = 'ens3'
    NETMASK = '255.255.255.0'

    def test_name_server(self):
        proc1 = subprocess.run(['cat /etc/resolv.conf | grep ' + '{}'.format(self.NAME_SERVER_IP)], shell=True)
        assert proc1.returncode == 0

    # def test_my_netmask(self):
    #     netmask = ni.ifaddresses(self.MY_INTERFACE)[ni.AF_INET][0]['netmask']
    #     assert netmask == self.NETMASK
        
    # def test_ping_google(self):
    #     response = subprocess.run(['ping', 'google.com', '-c 4'])
    #     assert response.returncode == 0
            
    # def test_ping_router(self):
    #     response = subprocess.run(['ping', self.ROUTER_IP, '-c 4'])
    #     assert response.returncode == 0
    
    # def test_ping_client_2(self):
    #     response = subprocess.run(['ping', self.CLIENT_2_IP, '-c 4'])
    #     assert response.returncode == 0

    # def test_ping_server(self):
    #     response = subprocess.run(['ping', self.SERVER_IP, '-c 4'])
    #     assert response.returncode == 0