"""
objects:
Iterable - __iter__()  or __getitem__()
Iterable - __next__()
Iteration -
"""


# for i in range(230000000):
def gen(n):
    for i in range(n):
        yield i


# g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# # print(g.__next__())
# # print(g.__next__())

# for i in g:
#     print(i)

h = "harry"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())