def generator(x, n) :
    c = [int(i) ** 2 for i in range(x, n)]
    for i in c : 
        if i / x == x :
            a +=1
            yield i

x, n = int(input("begin:")), int(input("end:"))
for s in generator(x, n) :
    print(s)


# def squares(a, b):
#     c = [int(i)**2 for i in range(a, b)]
#     for i in c:
#         j = a
#         if i / j == j:
#             print(i)
#         j += 1
#     yield i
# a = int(input("Begin: "))
# b = int(input("End: "))
# print(next(squares(a, b)))