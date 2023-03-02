"""
Напишите функцию  get_names_sorted(animals), которая возвращает в
формате списка строк названия всех животных отсортированных по алфавиту.
"""

animals = [{
  "specie": "Macaca fuscata",
  "color": "Khaki"
}, {
  "specie": "Cygnus atratus",
  "color": "Aquamarine"
}, {
  "specie": "Ursus arctos",
  "color": "Yellow"
}]


def get_names_sorted(animals_tuple):
    new_list = []
    for item in animals_tuple:
        new_list.append(item["specie"])
    new_list = list(sorted(new_list))
    return new_list


print(get_names_sorted(animals))
