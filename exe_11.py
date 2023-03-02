"""
У вас есть список всех задач, которые нужно сделать и три исполнителя,
которые решали эти задачи, выведите задачи, которые никто не решил.
"""

tasks = [
   "сходить в магазин" ,
   "купить гвозди",
   "полить сельдерей",
   "украсить елку",
   "нарисовать снежинку",
   "найти открытки"
]

emp_1 = ["купить гвозди", "найти открытки"]
emp_2 = ["полить сельдерей","сходить в магазин"]
emp_3 = ["найти открытки","купить гвозди"]


def get_unsolved_tasks(first_list, second_list, third_list, fourth_list):
    first_set = set(first_list)
    second_set = set(second_list)
    third_set = set(third_list)
    fourth_set = set(fourth_list)
    new_list = list(first_set.difference(second_set, third_set, fourth_set))
    print(new_list)


get_unsolved_tasks(tasks, emp_1, emp_2, emp_3)
