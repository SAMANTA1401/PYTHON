def compound_interest(p,r,t):
    amount = p*pow(1+(r/100), t)
    interest = amount-p
    print("compound interest is:",interest)
compound_interest(r=13, p=1000000, t=5) #passing keyword argument
compound_interest(1000000, 13, 5)  #passing positional argument