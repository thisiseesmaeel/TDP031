import subprocess
import sys
from randompass import generate_random_password
from usernamegen import generate_username


def create_user(fullname):
    user = {}
    firstname = fullname.split()[0]
    lastname = ""
    if(len(fullname.split()) > 1):
        lastname = "".join(fullname.split()[1:])

    # Trying to find a username that is not taken
    while(True):
        potential_username = generate_username(firstname, lastname)
        exist = subprocess.run(['getent', 'passwd', potential_username], stdout=subprocess.PIPE).stdout.decode('utf-8')
        if(len(exist) == 0):
            break


    user["first name"] = firstname
    user["last name"] = lastname
    user["username"] = potential_username
    user["password"] = "password" # generate_random_password() this should be a random but for test purposes 
                                 # can be "1234567"

    return user

def get_first_name(user):
    return user["first name"]

def get_last_name(user):
    return user["last name"]

def get_username(user):
    return user["username"]

def get_password(user):
    return user["password"]


def main():
    file_name = sys.argv[1]
    users = []

    with open (file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        users.append(create_user(line))
        
    for user in users:
        username = get_username(user)
        password = get_password(user)
        print("First name: {}\nLast name: {}\nUsername: {}\nPassword: {}\n".format(get_first_name(user), get_last_name(user), username, password))

        # If we want to give sudo to the user
        #subprocess.run(['useradd' , '-s', '/bin/bash', '-d', '/home/{}/'.format(username), '-m', '-G', 'sudo',  username])

        # If we don't want to give sudo to the user
        p1 = subprocess.run(['useradd' , '-s', '/bin/bash', '-d', '/home/{}/'.format(get_username(user)), '-m', get_username(user)])
        
        proc = subprocess.Popen(['passwd', username], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)  
        proc.stdin.write('{}\n'.format(password).encode('utf-8'))  
        proc.stdin.write('{}'.format(password).encode('utf-8'))
        proc.communicate("\n".encode("utf-8"))

    subprocess.run(['make', '-C', '/var/yp'])

#==================
if __name__ == "__main__":
    main()