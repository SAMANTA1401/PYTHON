# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
#
# print(ls)

# ls = [i for i in range(100)]
#
# print(ls)
#
# ls = [ i for i in range(100) if i%3==0]
#
# print(ls)

# dict1 = {i:f"item{i}" for i in range(100)}
# print(dict1)

# dict = {i:f"item{i}" for i in range(1, 10001) if i%100==0}
# print(dict)

# dict1 = {i:f"Item {i}" for i in range(5)}
# # to reverse  the dictionary dict1
# dict2 = {value:key for key,value in dict1.items()}
#
# print(dict1,"\n", dict2)

# set comprehension
# dresses = {dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2"]}
# print(type(dresses))
# print(dresses)
# # list comprehension
# dresses = [dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2"]]
# print(type(dresses))
# print(dresses)

evens = (i for i in range(100) if i%2==0)
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# for item in evens:
    # print(item)

# for_else

khana = ["roti","sabzi","chawal"]

# for item in khana:
#     print(item)
#     # break
# else:
#     print("This for loop ended properly")

for item in khana:
    if item == "paratrha":
        break

else:
    print("Your item was not found")