# TODO реализовать функцию
def get_unique_words(str_):
    uni = str_.split()
    uni2 = set(uni)
    uni3 = list[uni2]
    sort_ = uni3.sort()
    return sort_


print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
