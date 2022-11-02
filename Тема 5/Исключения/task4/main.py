# TODO написать функцию remove

from typing import Any
def remove(list_:list, value:Any) -> int:
    for i, current_value in enumerate(list_):
        if current_value == value:
            return list_[:1]+list_[i+1:]
    raise ValueError("Значение отсутствует")


print(remove([0, 0, 1, 2], 0))  # [0, 1]
print(remove([0, 1, 1, 2, 3], 1))  # [0, 1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
