file=open("D:\\MCA\\python\\file2.txt","w") #create and opening file
print(file)
file.write("hello how are you?\n") #writing content to file
file.write("second line is added\n")
file.close()

file2=open("D:\\MCA\\python\\file2.txt","r")
print(file2.read())

file.close()