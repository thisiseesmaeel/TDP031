
import unittest
import subprocess

class UgenTest(unittest.TestCase):
    def test_root_exist(self):
            exist = subprocess.run(['getent', 'passwd', 'root'], stdout=subprocess.PIPE).stdout.decode('utf-8')
            self.assertNotEqual(len(exist), 0, "root does not exist!")


    def test_games_has_no_shell(self):
        # Template
        #self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
        status = subprocess.run(['su', 'games'])
        self.assertEqual(status.returncode, 1, "Games has shell!")

        

if __name__ == '__main__':
    unittest.main()


#in order to run the test write pytest-3 -q testsuit.py
import subprocess

# class TestUgen:
#     def test_games_has_no_shell(self):
#         status = subprocess.run(['su', 'games'])
#         assert status.returncode == 1

#     def test_root_exist(self):
#         exist = subprocess.run(['getent', 'passwd', 'root'], stdout=subprocess.PIPE).stdout.decode('utf-8')
#         assert len(exist) != 0 

  

        