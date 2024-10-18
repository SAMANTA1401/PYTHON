# iterators

number_list = [23,4,45,12] #iterable
# for i in number_list:
#     print(i)
#iter() is a iterator
number_iter=iter(number_list)

# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))

squares =map(lambda a:a**2,number_list) #iterator
print(next(squares))
print(squares)


