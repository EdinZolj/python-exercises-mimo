# Variable created inside a function have a "local scope".

def add_bonus(salary):
    bonus = 100
    print(salary + bonus)

add_bonus(1900)


# Variables created outside of a function block have a "global scope".

shipping = 10

def calculate_total(cart):
    print(cart + shipping)

calculate_total(54)