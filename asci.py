# to print ASCII value of a given character : 
# c = 'g'
# print("The ASCII value of '" + c + "' is", ord(c))

print("Enter a string:", end="")
text = input()
textlength = len(text)
for char in text:
    ascii = ord(char)
    print(char, "\t", ascii)



