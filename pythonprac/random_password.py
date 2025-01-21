# Generate a random Password which meets the following conditions
# Password length must be 10 characters long.
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

import random
import string

def random_password():
    randomSource=string.ascii_letters+string.digits+string.punctuation
    print(randomSource)
    password=random.sample(randomSource,6)
    print(password)
    password+=random.sample(string.ascii_uppercase,2)
    print(password)
    password+=random.choice(string.digits)
    print(password)
    password+=random.choice(string.punctuation)
    print(password)
    passwordList=list(password)
    print(passwordList)
    random.SystemRandom().shuffle(passwordList)
    password="".join(passwordList)


    return password
print(random_password())