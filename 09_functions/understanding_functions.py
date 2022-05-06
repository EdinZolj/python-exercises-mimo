# Giving functions descriptive names like "get_final_price" helps us know at a glance wgar they do.
# Functions are actions, so their name often starts with a verb, like get, create, compute, calculate, generate etc..
# As a special case, functions that return boolean values often start with "is"

def get_final_price(price, tax):
    return price + tax

price = get_final_price(30, 1.5)
print(price)


def is_freezing(temperatur):
    return temperatur < 0

freezing = is_freezing(-3)
print(freezing)


def display_item_price(item, price):
    print(f"{item}: {price},- €")

display_item_price("chocolate", 3)


def generate_username(name, b_day):
    return (f"{name}_{b_day}")

user = generate_username("ty", 17)
print(user)


def get_successor(number):
    return number + 1

def get_predecessor(number):
    return number - 1

successor = get_successor(1)
print(successor)

predecessor = get_predecessor(1)
print(predecessor)