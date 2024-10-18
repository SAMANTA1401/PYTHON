import shutil
shutil.copy("D:\\MCA\\python\\file2.txt", "D:\\MCA\\python\\filenew1.txt")

with open("D:\\MCA\\python\\filenew1.txt","r") as file:
    print(file.read())