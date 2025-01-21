f1 = open("harry.txt")

try:
    f = open("does2.txt")


# except Exception as e:
#     print(e)
except EOFError as e:
    print("print eof error aa gaya hai", e)
except IOError as e:
    print("print io error aa gaya hai", e)

else:
    print("this will run only uf except is not running")
finally:
    print("Run this anyway...")
    f1.close()
print("Important stuff")

