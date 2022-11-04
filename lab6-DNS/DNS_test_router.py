import subprocess
import netifaces as ni

class TestDNSRouter:
    MY_IP = '10.0.0.1'
    CLIENT_1_IP = '10.0.0.2'
    CLIENT_2_IP = '10.0.0.3'
    NAME_SERVER_IP = '10.0.0.4'
    MY_INTERFACE = 'ens3'
    NETMASK = '255.255.255.0'

    def test_name_server(self):
        proc1 = subprocess.run(['cat /etc/resolv.conf | grep ' + '{}'.format(self.NAME_SERVER_IP)], shell=True)
        assert proc1.returncode == 0
    
    def test_forward_dig_server(self):
        result = subprocess.run(['dig', 'server.saysahadan.example.com', '+short'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert result.strip() == self.NAME_SERVER_IP 

    def test_forward_dig_client1(self):
        result = subprocess.run(['dig', 'client1.saysahadan.example.com', '+short'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert result.strip() == self.CLIENT_1_IP 

    def test_forward_dig_client2(self):
        result = subprocess.run(['dig', 'client2.saysahadan.example.com', '+short'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert result.strip() == self.CLIENT_2_IP 

    def test_reverse_dig_server(self):
        result = subprocess.run(['dig', '-x', self.NAME_SERVER_IP, '+short'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert result.strip() == "server."

    def test_reverse_dig_client1(self):
        result = subprocess.run(['dig', '-x', self.CLIENT_1_IP, '+short'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert result.strip() == "client1." 

    def test_reverse_dig_client2(self):
        result = subprocess.run(['dig', '-x', self.CLIENT_2_IP, '+short'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert result.strip() == "client2." 