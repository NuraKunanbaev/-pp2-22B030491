number = int(input("Write number: "))
even_n = [i for i in range(number) if i%2==0]
print("All even numbers up to {}".format(number))
print(*even_n,sep =", ")