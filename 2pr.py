# to check perfect number
# A number is a perfect number if is equal to sum of its proper divisors, that is, sum of its positive divisors excluding the number itself. 
#6>> 1+2+3 exclude 6
# 1*6=6
# 2*3=6


def isPerfect(n):

    # to store sum of divisior
    sum = 1

    # find all divisior and add them
    i = 2
    while i* i <= n:
        if n% i ==0:
             sum = sum + i + n/i
        i += 1
     
    # If sum of divisors is equal to
    # n, then n is a perfect number
     
    return (True if sum == n and n!=1 else False)
 
# Driver program
print("Below are all perfect numbers till 10000")
n = 2
for n in range (100):
    if isPerfect (n):
        print(n , " is a perfect number")
