from functools import reduce
data = [1, 2, 3, 4]
print(reduce(lambda x, y: x + y, data))