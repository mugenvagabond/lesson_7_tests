"""
Напишите функцию  filter_violet_only(animals), которая возвращает в
формате списка словари только тех животных, которые фиолетовые (violet)
"""

animals = [{
  "id": 1,
  "specie": "Eumetopias jubatus",
  "color": "Violet"
}, {
  "id": 2,
  "specie": "Tayassu tajacu",
  "color": "Violet"
}, {
  "id": 3,
  "specie": "Ephipplorhynchus senegalensis",
  "color": "Teal"
}, {
  "id": 4,
  "specie": "Pycnonotus barbatus",
  "color": "Indigo"
}, {
  "id": 5,
  "specie": "Acridotheres tristis",
  "color": "Violet"
}, {
  "id": 6,
  "specie": "Hippotragus niger",
  "color": "Teal"
}, {
  "id": 7,
  "specie": "Redunca redunca",
  "color": "Turquoise"
}]


def filter_violet_only(animals_tuple):
    new_tuple = []
    for item in animals_tuple:
        if item["color"] == "Violet":
            new_tuple.append(item)
    return new_tuple


print(filter_violet_only(animals))
