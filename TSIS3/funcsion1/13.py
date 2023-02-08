# guess the number
import random
def Guess_the_number(x):
    if x == y:
        global t
        t = False
        return print("Good job, {} ! You guessed my number in {} guesses!".format(s,sum))
    elif x <  y:
        print("Your guess is too low")
    elif x > y:
        print("Your guess is too high")

s = input("what is your name?\n")
print("Hell, {}, I guess from 1 to 20".format(s))
y = random.randint(1, 20)
sum = 0
t = True
if __name__ == '__main__' :

    while t != False:
        print("Take a guess.")
        x = int(input())
        sum+=1
        Guess_the_number(x)