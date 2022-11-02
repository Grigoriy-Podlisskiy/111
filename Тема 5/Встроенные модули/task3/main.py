# TODO заполнить список случайными числами

# TODO посчитать количество отрицательных чисел


from random import randint
start = -100
finish = 100
count = 51
list_numbers = [randint(start, finish)  for _ in range(count)]
nega = [num for num in list_numbers if num < 0]

print(list_numbers)
print(len(nega))
