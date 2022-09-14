import unittest
import subprocess

class UgenTest(unittest.TestCase):
    def test_root_exist(self):
            exist = subprocess.run(['getent', 'passwd', 'root'], stdout=subprocess.PIPE).stdout.decode('utf-8')
            self.assertNotEqual(len(exist), 0, "root does not exist!")


    def games_has_no_shell(self):
        # Template
        #self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
        false_cmd = subprocess.run('false')
        self.assertEqual(false_cmd.returncode, 2, "Games has shell!")

        

if __name__ == '__main__':
    unittest.main()