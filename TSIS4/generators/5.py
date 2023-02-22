number =  int(input("Write number: "))
back_s = [i for i in range(number,-1,-1)]

print(*back_s,sep="\n")