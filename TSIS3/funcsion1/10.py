#unique- только уникальные
def unique(l:list):
    unique_l = []
    for i in l:
        if i not in unique_l:
            #append- конец списка
            unique_l.append(i)
    print(unique_l)
if __name__ =='__main__' :
    l = [int(x) for x in input().split()]
    unique(l)