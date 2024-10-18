
    
    i=2
    while (i<n):
        
        r = n % i 
        if r==0:
            return False
        i = i+1
    
    print(n)
    return True


N =100
for n in range(N):
    isPrime(n)