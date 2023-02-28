import re
txt = input()
pat1 = '^a.*?b$'
x = re.search(pat1, txt)
if x:
    print("We found it")
else:
    print("We didn't find")
