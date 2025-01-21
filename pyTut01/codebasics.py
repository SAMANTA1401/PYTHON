# num = int(input("Enter a number: "))
# if num%2 ==0:
#     print("number is even")
# else:
#     print("number is odd")

tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]


def total(exp):
    total = 0
    for item in exp:
        total = total + item
    return  total

name = input()
list = f"{name}_exp_list"
arg=globals()[list]
print(total(arg))

