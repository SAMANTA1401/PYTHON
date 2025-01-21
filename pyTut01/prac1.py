yearAge = int(input("what is your Age/Year of birth"))
isAge = False
isYear= False

if len(str(yearAge)) == 4:
    isYear = True

else:
    isAge = True

if (yearAge<1900 and isYear):
    print("You seem to be the oldest person alive")
    exit()
if(yearAge>2019):
    print("you are not yet born")
    exit()

if isAge:
    yearAge = 2019 - yearAge

interestedYear = int(input("Enter the  year you want to know your age in\n"))
print(f"you will be 100 years old in {yearAge + 100}")

# if yearAge>125:
#     isAge = True
#
# elif yearAge>1900:
#     isYear = True
# elif(yearAge<1900):
#     print("You seem to be the oldest person alive")
#     exit()
# elif (yearAge > 2022):
#     print("You are not yet born")
#     exit()
#
# else:
#     print("There was some problem with your age/year ofbirth")
#     exit()
#
#
# if isAge:
#     p
