import decimal

students_dict = {
    'Саша': 27,
    'Кирилл': 52, 
    'Маша': 14, 
    'Петя': 36, 
    'Оля': 43, 
}

# TODO распечатать с использованием f-строк

for name, oc in students_dict.items():
    print(f'Студент {name} получил {oc} баллов')

x = 10
y = 10

print(f'x = {x}, y = {y}')

number = 253.3463
print(f'{f'${number:.3f}':>10s}')

value = decimal.Decimal("42.12345")
print(f'Result{value:{"10.5" if value < 100 else "8.3"}}')
value = decimal.Decimal("142.12345")
print(f'Result{value:{"4.2" if value < 100 else "8.3"}}')