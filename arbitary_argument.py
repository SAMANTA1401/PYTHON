def sum(*a):  #declaration of arbitary argument
    sum=0
    for i in a:
        sum = sum+i
    print("sum of series a is:",sum)

sum(1,2,3,4,5,6) #passing arbitary argument *args
