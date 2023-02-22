number = int(input("Write number:"))
f_numbers = [i for i in range(number) if i%3==0 and i%4==0]

print(*f_numbers,sep="\n")
