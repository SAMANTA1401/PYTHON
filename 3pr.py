# Given a number N, the task is to print the prime numbers from 1 to N.

# def isPrime(n):
#     i=2
#     while (i<n):
        
#         r = n % i 
#         if r==0:
#             return False
#         i = i+1
    
#     print(n)
#     return True


# N =100
# for n in range(N):
#     isPrime(n)

# Given two positive integers start and end. The task is to write a Python 
# program to print all Prime numbers in an Interval.
    
def prime(x,y):
    prime_list = []
    for n in range(x,y):
        def isPrime(n):
            i=2
            while (i<n):
                
                r = n % i 
                if r==0:
                    return False
                i = i+1
            
            return n
        isPrime(n)
        if isPrime(n)==n:
            prime_list.append(isPrime(n))
       
        
    return prime_list
        

print(prime(5, 15))


 



        
