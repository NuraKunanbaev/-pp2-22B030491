def generator(N):
    for i in range(1, N): 
        yield i**2


for x in generator(10):
    print(x)



# n = int(input())
# x = [i**2 for i in range(1, n)]
# print(x)