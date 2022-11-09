import subprocess
import netifaces as ni

class TestNISServer:
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

    def test_domain_dir1(self):
        directories = subprocess.run(['ls', '/var/yp'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
        assert self.NIS_DOMAIN in directories

    def test_domain_dir2(self):
        directories = subprocess.run(['ls', '/var/yp'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
        assert "ypservers" in directories