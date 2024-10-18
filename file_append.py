with open("D:\\MCA\\python\\file2.txt","a") as file: #to add new line in existing file without overwrite
    file.write("4th line is added")

with open("D:\\MCA\\python\\file2.txt","r") as file:
    print(file.read())
