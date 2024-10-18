# Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2.

def sumSqure(N):
    sum = 0
    for i in range(1,N+1):
        k = i*i
        # print(k)
        sum = sum + k
    return print(sum)
    

# sumSqure(5)

# Print the sum of series 13 + 23 + 33 + 43 + …….+ n3 till n-th term


def sumCube(N):
    sum = 0
    for i in range(1,N+1):
        k = i*i*i
        # print(k)
        sum = sum + k
    return print(sum)
    

# sumCube(5)

# Given an array of integers, find the sum of its elements.

def sumArr(arr):
    sum = 0
    # for i in range(len(arr)):
    #     sum = sum + arr[i]
    for i in arr:
        sum = sum + i

    return print(sum)

# arr= [4,15,3,124]
# sumArr(arr)

# Given an array, find the largest element in it.
# print(max(arr))

def largest(arr):
    maxm = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maxm:
            maxm = arr[i]
    return maxm

# largest(arr)

def largests(arr):
    arr.sort()
    return arr[len(arr)-1]

# print(largests(arr))

# Write a function 
# rotate(ar[], d, n) that rotates arr[] of size n by d elements.



def rotation(d):
    n =len(arr1)
    temp = []
    for i in range(d):
        temp.append(arr1[i])
    arr2 = arr1[d:] 
    arr3 = arr2 +temp
    # print(temp)
    # print(arr3)
    return arr3


arr1 = [1,2,3,4,5,6,7,9]
# rotation(2)


# Given multiple numbers and a number n, the task is 
# to print the remainder after multiplying all the numbers divided by n.

def arrMul(n):
    mul = 1
    for i  in range(len(arr1)):
        mul = mul * arr1[i]
    print(mul)
    k = mul % n
    return print(k)

# arrMul(17)

# Given an array of N elements and an integer M. Now, the arr
# ay is modified by replacing some of the array elements with 
# -1. The task is to print the original array.
# The elements in the original array are related as, for every
#  index i, a[i] = (a[i-1]+1)% M.
# It is guaranteed that there is one non-zero value in the array.

#  ??????????????

# Python implementation of the above approach
def construct(n, m, a):
    ind = 0
 
    # Finding the index which is not -1
    for i in range(n):
        if (a[i]!=-1):
            ind = i
            break
 
    # Calculating the values of the indexes ind-1 to 0
    for i in range(ind-1, -1, -1):
        if (a[i]==-1):
            a[i]=(a[i + 1]-1 + m)% m
 
    # Calculating the values of the indexes ind + 1 to n
    for i in range(ind + 1, n):
        if(a[i]==-1):
            a[i]=(a[i-1]+1)% m
    print(*a)
 
# Driver code
n, m = 6, 7
a =[5, -1, -1, 1, 2, 3]
# construct(n, m, a)

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].
#  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
arr = [1,2,3,7,5,6,7]
arr3 = arr[::-1]

def monotonic(arr):
    i=0
    if arr[i]<=arr[i+1]:
        while arr[i]<=arr[i+1]:
            if i<(len(arr)-2):
                i = i+1
            else:
                print('x')
                break
            print('z')

        if i==(len(arr)-2):
            print(i)
            return True
        else:
            print(i)
            return False
    else:
        while arr[i]>=arr[i+1]:
            if i<(len(arr)-2):
                i = i+1
            else:
                print('x')
                break
            print('z')

        if i==(len(arr)-2):
            print(i)
            return True
        else:
            print(i)
            return False


print(monotonic(arr3))


# reverse the array
# arr = [1,2,3,4,5,6,7]
# arr3 = arr[::-1]
# print(arr3)

