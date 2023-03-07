import os
path = os.path.abspath("regex")
print(path)
if os.path.exists(path):
    print("File exists")
else:
    print("File doesn't exist")
path2 = r'C:\Users\User\Desktop\python\pp2-22B030492\TSIS5\regex\ts_3.py'
if os.path.exists(path2):
    print("File exists")
    print(os.path.basename(path2))
    print(os.path.dirname(path2))
else:
    print("File doesn't exist")