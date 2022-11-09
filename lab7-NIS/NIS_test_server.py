import subprocess
import netifaces as ni

class TestDNSRouter:
    NIS_DOMAIN = 'nis.saysahadan.example.com'

    def test_nis_domain1(self):
        nis_domain = subprocess.run(['nisdomainname'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
        assert nis_domain.strip() == self.NIS_DOMAIN 

    def test_nis_domain2(self):
        nis_domain = subprocess.run(['cat', '/etc/defaultdomain'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
        assert nis_domain.strip() == self.NIS_DOMAIN

    def test_rpcbind_service(self):
        status = subprocess.run(['service', 'rpcbind', 'status'])
        assert status == 0 # 0 means the service is running 

    def test_ypserv_service(self):
        status = subprocess.run(['service', 'ypserv', 'status'])
        assert status == 0 # 0 means the service is running 