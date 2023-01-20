import subprocess
import re

class TestRawString:
    NTP_server = 'se.pool.ntp.org.'

    def test_raw_string(self):
        result = subprocess.run(['cat', 'config.txt'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert re.search(r'\nserver {}'.format(self.NTP_server), result) != None
