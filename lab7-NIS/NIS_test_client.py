import subprocess
import netifaces as ni
import re

class TestNISClient:
    NIS_DOMAIN = 'nis.saysahadan.example.com'

    def test_nis_domain1(self):
        nis_domain = subprocess.run(['nisdomainname'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
        assert nis_domain.strip() == self.NIS_DOMAIN 

    def test_nis_domain2(self):
        nis_domain = subprocess.run(['cat /etc/defaultdomain'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
        assert nis_domain.strip() == self.NIS_DOMAIN

    def test_rpcbind_service(self):
        status = subprocess.run(['service', 'rpcbind', 'status'])
        assert status.returncode == 0 # 0 means the service is running 

    def test_ypbind_service(self):
        status = subprocess.run(['service', 'ypbind', 'status'])
        assert status.returncode == 0 # 0 means the service is running 

    def test_nis_server(self):
        nis_server = subprocess.run(['ypwhich'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
        assert nis_server.strip() == "server"

    def test_nsswitch_conf_passwd():
        nsswitch_config = subprocess.run(['cat /etc/nsswitch.conf'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
        assert re.search(r'^passwd:\s*.* nis', nsswitch_config) != None

    def test_nsswitch_conf_group():
        nsswitch_config = subprocess.run(['cat /etc/nsswitch.conf'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
        assert re.search(r'^group:\s*.* nis', nsswitch_config) != None
    
    def test_nsswitch_conf_shadow():
        nsswitch_config = subprocess.run(['cat /etc/nsswitch.conf'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
        assert re.search(r'^shadow:\s*.* nis', nsswitch_config) != None