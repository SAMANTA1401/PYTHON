sentence =input("Enter a sentence: ")
construct_dictionary={"digits":0,"lowercase":0,"uppercase":0,"spec_char":0}

for each in sentence:
    if each.isdigit():
        construct_dictionary["digits"]=construct_dictionary["digits"] + 1
    elif each.isupper():
        construct_dictionary["uppercase"]=construct_dictionary["uppercase"] + 1
    elif each.islower():
        construct_dictionary["lowercase"]=construct_dictionary["lowercase"] + 1
    else:
        construct_dictionary["spec_char"]=construct_dictionary["spec_char"] + 1
print(construct_dictionary)    




