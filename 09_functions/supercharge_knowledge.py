# Replays of fundametals in this chapter.

import email
from time import process_time_ns


def is_valid(user_and_domain):
    print(len(user_and_domain) == 2)

email = "edin@gmail.com"
user_and_domain = email.split("@")
is_valid(user_and_domain)


def get_domain(email):
    return email[2]

email = ["laura", "@", "gmail.com"]
domain = get_domain(email)
print(domain)


def add_sports(plans):
    plans[0] = "jogging"

plans = ["reading", "bruch with Andrina", "cooking", "netflix"]
add_sports(plans)
print(plans)


def update_todos(todos):
    todos[2] = "call grandma"
    return todos

todo_list = ["homework", "walk oreo", "watch tv"]
new_list = update_todos(todo_list)
print(new_list)


