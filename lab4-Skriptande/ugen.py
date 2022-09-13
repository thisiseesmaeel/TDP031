import subprocess
import sys
import random
from randompass import generate_random_password
from usernamegen import generate_username


def create_user(fullname):
    user = {}
    firstname = fullname.split()[0]
    lastname = ""
    if(len(fullname.split()) > 1):
        lastname = fullname.split()[1]


    potential_username = generate_username(firstname, lastname)
    exist = input(subprocess.run(['getent', 'passwd', potential_username]))

    while(len(exist) != 0):
        potential_username = generate_username(firstname, lastname)
        exist = input(subprocess.run(['getent', 'passwd', potential_username]))

    user["first name"] = firstname
    user["last name"] = lastname
    user["username"] = generate_username(firstname, lastname)
    user["password"] = generate_random_password()

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
    names = []
    users = []

    with open (file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        users.append(create_user(line))
        
    for user in users:
        print("First name: {}\nLast name: {}\nUsername: {}\nPassword: {}\n".format(get_first_name(user), get_last_name(user), get_username(user), get_password(user)))

    # If we want to give sudo to the user
    #subprocess.run(['useradd' , '-s', '/bin/bash', '-d', '/home/{}/'.format(username), '-m', '-G', 'sudo',  username])

    # If we don't want to give sudo to the user
    # subprocess.run(['useradd' , '-s', '/bin/bash', '-d', '/home/{}/'.format(username), '-m', username])

    # password = "123456\n123456"

    # subprocess.run(['printf', password, '|', 'passwd', username])


#==================
if __name__ == "__main__":
    main()