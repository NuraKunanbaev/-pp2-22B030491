import re
t = input()
txt = '^' + t + '$'
x = re.search('^abb$' or '^abbb$', txt)
if x:
    print("We found it")
else:
    print("We didn't find")
