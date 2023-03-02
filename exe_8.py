"""
На внешнем сервере хранится список со вложенным словарем.
Напишите функцию load_names(url), которая превратит его в список вида:
"""
import requests

URL = "https://www.jsonkeeper.com/b/NPMT"


def load_names(url_name):
    response = requests.get(url_name)
    response_json = response.json()
    new_list = []
    for item in response_json:
        new_list.append(item["first_name"])
    return new_list


print(load_names(URL))
