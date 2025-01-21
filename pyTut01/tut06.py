"""lambda function"""


#
# def add(a,b):
#     return a+b

# minus = lambda x, y: x-y
#
# print(minus(9, 4))


# def minus(x,y):
#     return x-y
#
# print(minus(9, 4))
#
# def a_first(a):
#     return a[1]
#
# a = [[1,2],[3,62],[8,9]]
# a.sort(key=a_first)
# print(a)
"""
client_list = {1:"harry",2:"soyel",3:"bappa",4:"sourav"}
log_list = {1:"exercise", 2:"diet"}

def getdate():
    import datetime
    return datetime.datetime.now()
print(str(getdate()))
try:
    print("select client name:")
    for key, value in client_list.items():
        # print(key)
        # print(value)
        print("press ", key ,"for ", value,"\n", end="")
    client_name = int(input())
    print("selected client name: ",client_list[client_name], "\n",end="")
    a = client_name
    if client_name==a:
        print("press 1 for log:")
        print("press 2 for retrieve:")
        op = int(input())
        if op==1:
            for key,value in log_list.items():
                print("press", key, "to log ",value, "\n", end="")
            log_name = int(input())
            print("selected job:", log_list[log_name])
            if log_name ==1:
                text = input("type here:")
                with open(f"{client_list[client_name]}ex.txt", "a") as opr:
                    opr.write(str([str(getdate())])+": "+text+ "\n")
                print("successfully logged.")
            elif log_name ==2:
                text = input("type here:")
                with open(f"{client_list[client_name]}diet.txt", "a") as opr:
                    opr.write(str([str(getdate())])+": "+text+ "\n")
                print("successfully logged.")
            else:
                print("enter valid input: 1 or 2")
        elif op==2:
            for key,value in log_list.items():
                print("press", key, "to log ",value, "\n", end="")
            log_name = int(input())
            print("selected job:", log_list[log_name])
            if log_name ==1:
                with open(f"{client_list[client_name]}ex.txt") as op:
                    for line in op:
                        print(line,end="")
            elif log_name==2:
                with open(f"{client_list[client_name]}diet.txt") as op:
                    for line in op:
                        print(line, end="")
            else:
                print("enter valid input: 1 or 2")
        else:
            print("enter valid input: 1 or 2")
    else:
        print("enter valid input: 1/2/3/4")

except Exception as e:
    print(e)
"""
"""random function """
"""
import random

random_number = random.randint(0,1)
# print(random_number)
rand = random.random()*100
# print(rand)
lst = ["star plus","dd1","aaj tak","code with harry"]
choice = random.choice(lst)
print(choice) 
"""
"""f" string"""
me = "harry"
a1 = 3
# a = "this is %s %s"%(me,a1)
# a = "this is {1} {0}"
# b = a.format(me,a1)
# print(b)

a = f"this is {me} {a1}"
print(a)