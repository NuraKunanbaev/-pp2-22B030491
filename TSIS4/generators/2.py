def generator(n) :
     for i in range(0, n) :
          yield i ** 2 

n = int(input("Write number"))
for x in generator(n) :
     print(x)









# number = int(input("Write number: "))
# even_n = [i for i in range(number) if i%2==0]
# print("All even numbers up to {}".format(number))
# print(*even_n,sep =", ")