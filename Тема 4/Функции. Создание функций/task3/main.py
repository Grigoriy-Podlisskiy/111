# TODO запишите здесь функцию factorial


# TODO распечатать результат выполнения функции factorial от числа 5


def factorial(n):
    number = 1
    for i in range(1, n+1):
        number *= i
    print(number)


factorial(5)