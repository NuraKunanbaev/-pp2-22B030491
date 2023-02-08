# reverse
def foo(st) :
    rev = st.split()
    rev.reverse()
    # соединение  их с помощью функции join()
    print(' '.join(rev))
st = input()
if __name__ == '__main__' :
    foo(st)