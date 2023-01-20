from difflib import restore
import subprocess
import netifaces as ni

class TestDNSServer:
    MY_IP = '10.0.0.4'
    CLIENT_1_IP = '10.0.0.2'
    CLIENT_2_IP = '10.0.0.3'
    ROUTER_IP = '10.0.0.1'

    def test_name_server(self):
        proc1 = subprocess.run(['cat /etc/resolv.conf | grep ' + '{}'.format(self.MY_IP)], shell=True)
        assert proc1.returncode == 0

    def test_bind9_config(self):
        proc1 = subprocess.run(['named-checkconf /etc/bind/named.conf.local'], shell=True)
        assert proc1.returncode == 0
        
    def test_zone(self):
        result = subprocess.run(['named-checkzone', 'saysahadan.example.com', '/etc/bind/zones/saysahadan.example.com'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert result.endswith("OK\n") 
            
    def test_forward_dig_router(self):
        result = subprocess.run(['dig', 'gw.saysahadan.example.com', '@localhost','+short'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert result.strip() == self.ROUTER_IP 

    def test_forward_dig_client1(self):
        result = subprocess.run(['dig', 'client1.saysahadan.example.com', '@localhost','+short'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert result.strip() == self.CLIENT_1_IP 

    def test_forward_dig_client2(self):
        result = subprocess.run(['dig', 'client2.saysahadan.example.com', '@localhost','+short'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert result.strip() == self.CLIENT_2_IP 

    def test_reverse_dig_router(self):
        result = subprocess.run(['dig', '-x', self.ROUTER_IP, '+short'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert result.strip() == "gw.saysahadan.example.com.0.0.10.in-addr.arpa."

    def test_reverse_dig_client1(self):
        result = subprocess.run(['dig', '-x', self.CLIENT_1_IP, '+short'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert result.strip() == "client1.saysahadan.example.com.0.0.10.in-addr.arpa." 

    def test_reverse_dig_client2(self):
        result = subprocess.run(['dig', '-x', self.CLIENT_2_IP, '+short'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert result.strip() == "client2.saysahadan.example.com.0.0.10.in-addr.arpa." 