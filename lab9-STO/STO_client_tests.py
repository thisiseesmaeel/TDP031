import subprocess
import re
import netifaces as ni

class TestSTOServer:
    CLIENT1_IP = "10.0.0.2"
    CLIENT2_IP = "10.0.0.3"
    SERVER_IP = "10.0.0.4"

    def test_verify_upstart_mount_usr_local(self):
        result = subprocess.run(['cat', '/etc/fstab'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert re.search(r'\n{}'.format(self.SERVER_IP), result) != None

