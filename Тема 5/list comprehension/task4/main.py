students_list = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36,
    },
    {
        "name": "Оля",
        "age": 43,
    },
]

# TODO посчитать средний возраст

# TODO распечатать список словарей студентов, возраст которых меньше среднего
ages_list = [s ['age'] for s in students_list]
average = sum(ages_list) / len(ages_list)
students_rugrats = [s for s in students_list if ]
