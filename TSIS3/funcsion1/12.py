#histogram
def histogram(l:list):
    for i in l:
        print(" * " * i)

if __name__ == "__main__" :
    l = [int(x) for x in input().split()]
    histogram(l)