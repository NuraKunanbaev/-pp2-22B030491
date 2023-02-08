# Polindrome
def palindrome(s):
    s2 = s[::-1]
    if s2 == s:
        print("YES")
    else:
        print("No")
if __name__ =='__main__' :
    s = input("This word is polindrome?: ")
    palindrome(s)