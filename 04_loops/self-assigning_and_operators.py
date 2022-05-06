# "self-assignment" is when we set a variable to its own value.

wallet = 3
wallet = wallet
print(wallet)

wallet = 3
wallet = wallet + 1
print(wallet)

name = "Account name:"
name = name + " Elton"
name = name + " John"
print(name)


# Programm that updates how many cars we've rented and how many are available.

total = 100
rented_cars = 50
available = total - rented_cars

print(f"{available} available cars")

rented_cars += 3
available = total - rented_cars

print(f"{available} available cars")


# Programm that keeps track of email inbox and how many unread emails we have.

unread = 54

print(f"You have {unread} unread emails")

new = 5
unread = unread + new

print(f"You got {new} new emails")
print(f"You have now {unread} unread emails")