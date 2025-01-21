# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a
# special symbol.
# : String must be the combination of the UPPER case and lower case letters only. No numbers and a
# special symbol.
import random
import string

def randomstring(stringLength):
    """ generate random string of length 5"""
    letters = string.ascii_letters
    ran_let = "".join(random.choice(letters))
    print(ran_let)
    return "".join(random.choice(letters) for i in range(stringLength))

print(randomstring(5))