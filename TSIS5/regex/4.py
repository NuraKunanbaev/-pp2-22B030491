import re
def find():
    patterns = "^[A-Z]+[a-z]+$"
    text = input()
    if re.search(patterns, text):
        print("eeeeeee bodyyyy, lightweight")
    else:
        print("oooo myy goood")
find()

