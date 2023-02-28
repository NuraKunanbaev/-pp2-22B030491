import re
txt = 'Nurtay is very strong, very smart and very attractive.'
x = re.sub("[ ,.]" , ":", txt)
print(x)
