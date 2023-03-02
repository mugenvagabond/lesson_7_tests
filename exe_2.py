"""
Напишите функцию, которая печатает имена из списка словарей в таком формате:
Kingsley
Tobit
Pace
Andreas
Anthia
"""

users = [{
        "id": 1,
        "first_name": "Anthia",
        "url": "https://weather.com/aliquet/at/feugiat/non/pretium.jsp"
    }, {
        "id": 2,
        "first_name": "Tobit",
        "url": "http://pen.io/sapien/cursus/vestibulum/proin/eu/mi/nulla.json"
    }, {
        "id": 3,
        "first_name": "Pace",
        "url": "http://ucsd.edu/justo/morbi/ut/odio/cras/mi.json"
    }, {
        "id": 4,
        "first_name": "Andreas",
        "url": "https://ifeng.com/morbi/vestibulum/velit.png"
    }, {
        "id": 5,
        "first_name": "Anthia",
        "url": "https://google.com/eu/orci.aspx"
    }, {
        "id": 6,
        "first_name": "Tobit",
        "url": "https://google.com/eu/orci.aspx"
    }, {
        "id": 7,
        "first_name": "Kingsley",
        "url": "https://google.com/eu/orci.aspx"
    },
    ]


def get_names_from_user_list(usernames):
    new_list = []
    for item in usernames:
        new_list.append(item["first_name"])
    new_list = list(set(new_list))
    for item in new_list:
        print(item)


get_names_from_user_list(users)

