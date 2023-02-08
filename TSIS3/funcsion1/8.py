def spy_games(l:list):
    s = ""
    #диапазон
    for i in range(len(l)):
        s+=str(l[i])
    s2 = ""
    for i in s:
        if i == '0' or i == '7':
            s2+=i
        else:
            continue
    if s2.find("007")+1 > 0:
        print("True")
    else:
        print("False")

if __name__ == '__main__' :
    l = [int(x) for x in input().split()]
    spy_games(l)