number = 2342354235235

list_digits = [int(d) for d in str(number)]  # TODO c помощью list comprehension получить список цифр числа

print(sum(list_digits))  # TODO найти сумму цифр числа
print(sum([s for s in list_digits if s % 2 == 0]))  # TODO найти сумму всех четных чисел
print(...)  # TODO найти количество цифр
print(...)  # TODO найти минимальную цифру
print(...)  # TODO найти разность между первой и последней цифрой
