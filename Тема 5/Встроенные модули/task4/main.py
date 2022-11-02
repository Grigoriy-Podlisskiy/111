# TODO написать функцию, которая выдает трехзначное число
from random import randint

def get_number():
    random = [randint(0,9) for _ in range(3)]
    str_number = "".join([str(digit) for digit in random])
    return int(str_number)
print(get_number())