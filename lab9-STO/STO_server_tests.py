import subprocess
import re
import netifaces as ni

class TestSTOServer:
    CLIENT1_IP = "10.0.0.2"
    CLIENT2_IP = "10.0.0.3"
    SERVER_IP = "10.0.0.4"

    # Test for checking if home1 and home2 are exported to the both clients (client1 and client2)
    def test_verify_client_exports(self):
        result = subprocess.run(['exportfs', '-s'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert re.search(r'\n\/home1\s+{}'.format(self.CLIENT1_IP), result) != None
        assert re.search(r'\n\/home2\s+{}'.format(self.CLIENT1_IP), result) != None
        assert re.search(r'\n\/home1\s+{}'.format(self.CLIENT2_IP), result) != None
        assert re.search(r'\n\/home2\s+{}'.format(self.CLIENT2_IP), result) != None

    def test_verfiy_access_rights(self):
        result = subprocess.run(['cat', '/etc/ntp.conf'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert re.search(r'\nserver {}'.format(self.NTP_server_IP), result) != None
    
    # def test_gw_respond_to_queries(self):
    #     proc1 = subprocess.Popen(['ntpq', '-p'], stdout=subprocess.PIPE)
    #     proc2 = subprocess.Popen(['grep', "gw"], stdout=subprocess.PIPE, stdin=proc1.stdout)
    #     proc1.stdout.close()
    #     output, err = proc2.communicate()
    #     output = output.decode('utf-8')
    #     ntp_server = output.split()[0]
        
    #     assert re.search(r'gw', ntp_server) != None

    # # Complete this test
    # def test_response_time(self):
    #     proc1 = subprocess.Popen(['ntpq', '-p'], stdout=subprocess.PIPE)
    #     proc2 = subprocess.Popen(['grep', "gw"], stdout=subprocess.PIPE, stdin=proc1.stdout)
    #     proc1.stdout.close()
    #     output, err = proc2.communicate()
    #     output = output.decode('utf-8')
    #     offset = abs(float(output.split()[-1]))

    #   assert offset <= self.REASONABLE_OFFSET