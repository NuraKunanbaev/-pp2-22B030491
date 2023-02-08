#classic puzle
def foo(numheads, numlegs) :
    all = numheads * 2
    x = numlegs - all
    rabbits = x // 2
    chicen = numheads - rabbits
    print(rabbits, chicen, sep=' ')
numheads = 35
numlegs = 94
foo(numheads, numlegs)

