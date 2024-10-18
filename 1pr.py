# geeks for geeks
# to interchange first and last element in list

# def swapList(newList):
#     size = len(newList)

#     # swaping
#     temp = newList[0]
#     newList[0] = newList[size-1]
#     newList[size-1] = temp

#     return newList

 
# def swapList(newList):
#     size = len(newList)

#     # swaping
#     newList[0], newList[-1] = newList[-1], newList[0]

#     return newList


# def swapList(newList):
#     size = len(newList)

#     # swaping
#     get = newList[0], newList[-1] 
#     newList[-1], newList[0] = get

#     return newList



newList =  [12,23,45,7,4]

# a, *b, c = newList

# print(a, b, c)


# def swapList(newList):

#     start, *middle, end = newList
#     newList = end, *middle, start

#     return newList


def swapList(newList):
    
    first = newList.pop(0)
    last = newList.pop(-1)

    newList.insert(0, last)
    newList.append(first)

    return newList

print(swapList(newList))
