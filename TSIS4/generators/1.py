def gensquares(N):
    for i in range(1, N): 
        yield i**2




N = int(input())
for x in gensquares(N):
    print(x)
