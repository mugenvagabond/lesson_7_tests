"""
У вас есть два списка. Напишите функцию count_unique которая вернет количество уникальных
в первом списке (входящих в первый, но не входящих во второй)
"""


def count_unique(first_set, second_set):
    set_one = set(first_set)
    set_second = set(second_set)
    new_set = set_one.difference(set_second)
    return len(new_set)


first = [1,2,3,4,5]
second = [4,5,6,7]


result = count_unique(first, second)
print(result)
