"""
Напишите функцию `filter_yellow_only(animals)`, которая выводит только тех животных, которые желтые (yellow)

Пример вывода:
Francolinus coqui is Yellow
Petaurus norfolcensis is Yellow

animals = [{
  "id": 1,
  "specie": "Francolinus coqui",
  "color": "Yellow"
}, {
  "id": 2,
  "specie": "Petaurus norfolcensis",
  "color": "Yellow"
}, {
  "id": 3,
  "specie": "Pseudoleistes virescens",
  "color": "Teal"
}, {
  "id": 4,
  "specie": "Sula dactylatra",
  "color": "Maroon"
}, {
  "id": 5,
  "specie": "Echimys chrysurus",
  "color": "Teal"
}]
"""

animals = [{
  "id": 1,
  "specie": "Francolinus coqui",
  "color": "Yellow"
}, {
  "id": 2,
  "specie": "Petaurus norfolcensis",
  "color": "Yellow"
}, {
  "id": 3,
  "specie": "Pseudoleistes virescens",
  "color": "Teal"
}, {
  "id": 4,
  "specie": "Sula dactylatra",
  "color": "Maroon"
}, {
  "id": 5,
  "specie": "Echimys chrysurus",
  "color": "Teal"
}]


def filter_yellow_only(animals_items):
    for item in animals_items:
        if item["color"] == "Yellow":
            print(f'{item["specie"]} is {item["color"]}')


filter_yellow_only(animals)
