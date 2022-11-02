def is_palindrome(str_):
    str_new = "".join(str_.lower().split())  # TODO привести строку к единому регистру и избавиться от пробелов
    print = str_new


    if str_ == str:  # TODO проверка палиндрома
        print("Строка палиндром")
    else:
        print("Строка не палиндром")


is_palindrome("Кит на море не романтик")
is_palindrome("Прочая строка")
