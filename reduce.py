from functools import reduce
numbers=[23,56,2,3,4,6,]
def sum(a,b):
    return a+b
a=reduce(sum,numbers)

print(a)