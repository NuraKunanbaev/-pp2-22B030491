import re
t = input()
txt = '^' + t + '$'
pat1 = 'ab*'
pat2 = '^a0$'
x = re.search(pat1 or pat2, txt)
if x:
    print("We found it")
else:
    print("We didn't find")
