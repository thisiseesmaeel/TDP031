import subprocess
import re
import netifaces as ni

class TestSTOServer:
    SERVER_REGEX_IP = "10\.0\.0\.4"

    def test_verify_upstart_mount_usr_local(self):
        result = subprocess.run(['cat', '/etc/fstab'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert re.search(r'\n{}'.format(self.SERVER_REGEX_IP), result) != None

    # Verify that nis is used for auto.master
    def test_verify_nis(self):
        result = subprocess.run(['cat', '/etc/nsswitch.conf'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert re.search(r'\nautomount:((\s+)|(.* ))nis', result) != None

