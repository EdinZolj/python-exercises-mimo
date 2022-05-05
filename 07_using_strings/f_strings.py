#Using f-strings to code a programm that tracks an online store's orders and stocks.

stock = 74
item = "webcams"
orders = 18

print(f"{stock} {item} in stock")
print(f"{orders} customer orders")
print(f"{stock - orders} available")

#A tip calculator for the next evening out.

bill = 20
tip_percentage = 0.15
tax_percentage = 0.067

tip = bill * tip_percentage
print(f"Tip: € {tip}")

tax = bill * tax_percentage
print(f"Tax: € {tax}")

total = bill + tip + tax
print(f"Total: € {total}")