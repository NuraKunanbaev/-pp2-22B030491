def num_of_letters(s):
    sum1 = 0
    sum2 = 0
    for i in s:
         if i.islower():
             sum1+=1
         elif i.isupper():
             sum2+=1
    print('num of upper letters:', sum1)
    print('num of lower letters:', sum2)
s = input("Enter the string: ")
num_of_letters(s)