from functools import reduce
newList = list((1, 2, 3, 10))
print(reduce(lambda x, y: x * y, newList))
