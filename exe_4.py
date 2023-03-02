"""
Напишите функцию  filter_violet_only(animals), которая возвращает в формате
списка id только тех животных, которые фиолетовые (violet)

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
    list_violet = []
    for item in animals_tuple:
        if item["color"] == "Violet":
            list_violet.append(item["id"])
    list_violet = list(sorted(list_violet))
    for id in list_violet:
        return list_violet


print(filter_violet_only(animals))
