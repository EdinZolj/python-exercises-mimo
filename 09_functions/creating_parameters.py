# Sometimes functions need specific info to help them perform their tasks. Like a function tht adds a players name to the team.
# Instead of writing two functions, we can pass specific infromation like "Leslie" to just one function, without repeating it.
# To pass a value to a function, we first add a variable called a "parameter" inside the parentheses of the function.
# Here well pass "name". The parameter, here "name", acts like a variable that stores a value.

def greet(name):
    print(f"Hello {name}!")

greet("April")
greet("Leslie")


#Functions need "multible paramenters" to perform tasks on more pieces of data, like a new players first and last name.

def display(first_name, last_name):
    print(first_name + " " + last_name)

display("Edin", "Zolj")


def show_winners(first, second, third):
    print("First place: " + first)
    print("Second place: " + second)
    print("Third place: " + third)

show_winners("Andrina", "Edin", "Edina")


def create_email(name, year):
    return name + year + "@hutmail.com"

email = create_email("jo", "1998")
print(email)