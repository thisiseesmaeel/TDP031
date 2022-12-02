import random
import string
import unicodedata

# Returns a username of lenght 9 in format of
# 3 firts letters in firstname + 2 first letters in lastname + 3 random digits
# Example: Sven Persson => svepe345
def generate_username(firstname = "", lastname = ""):

    firstname = unicodedata.normalize('NFKD', firstname).encode('ascii', 'ignore').decode('ascii')
    lastname = unicodedata.normalize('NFKD', lastname).encode('ascii', 'ignore').decode('ascii')

    firstname = ''.join(ch for ch in firstname if ch.isalnum())
    lastname = ''.join(ch for ch in lastname if ch.isalnum())

    string_part = ""
    if(len(firstname) < 3):
        string_part += generate_random_string(3)
    else:
        string_part += firstname[:3]
    if(len(lastname) < 2):
        string_part += generate_random_string(2)
    else:
        string_part += lastname[:2]

    username = (string_part + str(random.randint(100, 999))).lower()
    return username





def generate_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str