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


