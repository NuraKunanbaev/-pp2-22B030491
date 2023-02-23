# number =  int(input("Write number: "))
# back_s = [i for i in range(number,-1,-1)]

# print(*back_s,sep="\n")
def generators(n) :
    for i in range(n, -1, -1) :
        yield i

n = int(input("write number:"))
for x in generators(n) :
    print(x)