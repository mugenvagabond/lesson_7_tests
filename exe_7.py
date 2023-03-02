"""
Напишите функцию  get_comments_by_post_id(comments, post_id) которая возврашает
только те комментарии, которые к определенному посту
"""

comments = [{
  "author": "Werner",
  "time": "2:14 PM",
  "comment": "Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi.",
  "post_id": 3
}, {
  "author": "Raymond",
  "time": "12:48 PM",
  "comment": "Praesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.",
  "post_id": 5
}, {
  "author": "Silvio",
  "time": "2:45 PM",
  "comment": "Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.",
  "post_id": 1
}, {
  "author": "Shelbi",
  "time": "1:29 AM",
  "comment": "Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.",
  "post_id": 5
}, {
  "author": "Barnabas",
  "time": "2:28 PM",
  "comment": "Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.",
  "post_id": 5
}, {
  "author": "Mariellen",
  "time": "6:51 AM",
  "comment": "Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.",
  "post_id": 1
}, {
  "author": "Brandon",
  "time": "1:29 AM",
  "comment": "Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.",
  "post_id": 2
}]


def get_comments_by_post_id(comments_tuple, id_post):
    new_tuple = []
    for item in comments_tuple:
        if id_post == item["post_id"]:
            new_tuple.append(item)
    return new_tuple


print(get_comments_by_post_id(comments, 1))
