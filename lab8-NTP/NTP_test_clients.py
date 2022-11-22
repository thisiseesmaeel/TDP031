import subprocess
import re
import netifaces as ni

class TestDNSClient1:
    NTP_server_IP = '10.0.0.1' # gw IP address
    REASONABLE_OFFSET = 10  # Reasoable offset in millisecond

    def test_ntp_service(self):
        status = subprocess.run(['service', 'ntp', 'status'])
        assert status.returncode == 0 # 0 means the service is running 

    def test_ntp_server_config(self):
        result = subprocess.run(['cat', '/etc/ntp.conf'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert re.search(r'\nserver {}'.format(self.NTP_server_IP), result) != None
    
    def test_gw_respond_to_queries(self):
        proc1 = subprocess.Popen(['ntpq', '-p'], stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(['grep', "gw"], stdout=subprocess.PIPE, stdin=proc1.stdout)
        proc1.stdout.close()
        output, err = proc2.communicate()
        output = output.decode('utf-8')
        ntp_server = output.split()[0]
        
        assert re.search(r'gw', ntp_server) != None

    # Complete this test
    def test_response_time(self):
        proc1 = subprocess.Popen(['ntpq', '-p'], stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(['grep', "gw"], stdout=subprocess.PIPE, stdin=proc1.stdout)
        proc1.stdout.close()
        output, err = proc2.communicate()
        output = output.decode('utf-8')
        offset = abs(float(output.split()[-1]))

        assert offset <= self.REASONABLE_OFFSET