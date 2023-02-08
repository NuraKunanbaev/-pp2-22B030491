# Программа Python для печати всех
# перестановки с использованием библиотечной функции
from itertools import permutations
def foo(s) :
    perm = permutations(s)
    for i in list(perm):
        #соедините и распечатайте их с помощью функции join()
        print(''.join(i))
# Распечатать полученные перестановки
s = input()
if __name__ == '__main__' :
    foo(s)