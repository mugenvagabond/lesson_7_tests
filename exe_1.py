"""
Напишите функцию `get_unique_names(names)`, которая принимает
список и возвращает уникальные элементы из него в виде списка.

def get_unique_names(names):
    pass


names = ["Yvor", "Wendell", "Hogan", "Sadella", "Yvor", "Sadella", "Hogan"]

unique_names = get_unique_names(names)

print(unique_names)
"""


def get_unique_names(list_n):
    unique_list = list(set(list_n))
    return unique_list


names = ["Yvor", "Wendell", "Hogan", "Sabella", "Yvor", "Sadella", "Hogan"]

unique_names = get_unique_names(names)

print(unique_names)
