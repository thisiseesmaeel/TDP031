import subprocess
username = "Maghsood"

#subprocess.run(['echo', 'Hello'])

# If we want to give sudo to the user
#subprocess.run(['useradd' , '-s', '/bin/bash', '-d', '/home/{}/'.format(username), '-m', '-G', 'sudo',  username])

# If we don't want to give sudo to the user
subprocess.run(['useradd' , '-s', '/bin/bash', '-d', '/home/{}/'.format(username), '-m', username])

password = "123456\n123456"

subprocess.run(['printf', password, '|', 'passwd', username])