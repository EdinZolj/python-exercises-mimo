
def add_shipping(cart):
    if cart < 100:
        print(f"Total: {cart + 10}")
    else:
        print(f"Total: {cart}")

add_shipping(45)
add_shipping(200)


def calculate(operator, x, y):
    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    else:
        print(f"Unknown: {operator}")

calculate("-", 30, 10)