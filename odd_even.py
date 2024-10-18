# num = int(input("Enter a number: "))
# if num % 2 ==0:
#     print(num," is a even number.")
# else:
#     print(num," is a odd number")


# number grading system

score = float(input("Enter your score: "))
if score>1 or score<0:
    print("wrong Input")
elif score >= 0.9:
    print('your Grade is "A" ')
elif score >= 0.8:
    print('Your Grade is "B" ')
elif score >= 0.7:
    print('Your Grade is "C" ')
elif score >= 0.6:
    print('Your Grade is "D" ')
else:
    print('Your Grade is "F" ')
