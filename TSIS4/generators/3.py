def generator(n):
    for i in range(0, n) :
        if i % 3 == 0 and i % 4 == 0 :
            yield i 

n = int(input("write number"))
for x in  generator(n) :
    print(x)




# number = int(input("Write number:"))
# f_numbers = [i for i in range(number) if i%3==0 and i%4==0]

# print(*f_numbers,sep="\n")
