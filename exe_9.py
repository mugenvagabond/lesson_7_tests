"""
У вас есть два списка. Напишите функцию count_common(first,second),
которая возвращает, сколько элементов у них общие.
"""


def count_common(first_set, second_set):
    set_one = set(first_set)
    set_second = set(second_set)
    new_set = set_one.intersection(set_second)
    print(len(new_set))


first = [1,2,3,4,5]
second = [4,5,6,7]


count_common(first, second)
