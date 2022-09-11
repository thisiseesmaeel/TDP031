import subprocess
import sys
import random
import unicodedata


def create_qqqquser(fullname):
    user = {}
    user["first name"] = fullname.split()[0]
    user["last name"] = fullname.split()[1]
    user["user name"] = (fullname.split()[0][0:3] + fullname.split()[1][:2] + str(random.randint(100, 999))).lower()
    user["password"] = ""

    return 

def main():
    file_name = sys.argv[1]
    names = []
    user_names = {}

    with open (file_name, 'r', encoding='latin_1') as f:
        content = f.read()
        names.append(content)

    for name in names:
        print(name)
    
    username = "Maghsood"

    # If we want to give sudo to the user
    #subprocess.run(['useradd' , '-s', '/bin/bash', '-d', '/home/{}/'.format(username), '-m', '-G', 'sudo',  username])

    # If we don't want to give sudo to the user
    # subprocess.run(['useradd' , '-s', '/bin/bash', '-d', '/home/{}/'.format(username), '-m', username])

    # password = "123456\n123456"

    # subprocess.run(['printf', password, '|', 'passwd', username])


#==================
if __name__ == "__main__":
    main()