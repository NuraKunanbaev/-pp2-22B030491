def foo(num) :
    # определяем x переменную
    x = False
    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        # проверка
        for i in range(2, num):
            if (num % i) == 0:
                # если коэффициент найден, установить флаг в x
                x = True
                # стоп
                break

        # проверить, установлен ли флаг x
        if x:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
num = int(input())
foo(num)