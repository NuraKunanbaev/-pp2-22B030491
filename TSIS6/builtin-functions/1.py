import math
def multiply(l):
    return (math.prod(l))
l = [int(x) for x in input("Enter the numbers: ").split()]
print(multiply(l))
