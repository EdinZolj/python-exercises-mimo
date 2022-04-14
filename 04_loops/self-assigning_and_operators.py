#"self-assignment" is when we set a variable to its own value.

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


#Programm that updates how many cars we've rented and how many are available.

total = 100
rented_cars = 50
available = total - rented_cars

print(f"{available} available cars")

rented_cars += 3
available = total - rented_cars

print(f"{available} available cars")