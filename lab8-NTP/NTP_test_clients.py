import subprocess
import re
import netifaces as ni

class TestDNSClient1:
    NTP_server = '10.0.0.1' # gw IP address

    def test_ntp_service(self):
        status = subprocess.run(['service', 'ntp', 'status'])
        assert status.returncode == 0 # 0 means the service is running 

    def test_ntp_server_config(self):
        result = subprocess.run(['cat', '/etc/ntp.conf'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert re.search(r'\nserver {}'.format(self.NTP_server), result) != None
    
    def test_gw_respond_to_queries(self):
        result = subprocess.run(['ntpq', '-p', '|', "awk '{print $1}'", '|', 'grep "gw"'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert result == "gw"