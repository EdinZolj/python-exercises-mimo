# Program use if, elif and else statements to code a shipping cost calculator. 
# It will save the destination type and total purchase cost in variables, then update the shipping cost based on the destination.
# The higher the total, the cheaper the shipping cost.

international_shipping = True

total = 150
shipping_cost = 0

if international_shipping:
    shipping_cost += 15
    print("International base cost applied")    # to inform the user about the extra cost.

if total <= 50:
    shipping_cost += 20
elif total <= 100:
    shipping_cost += 15
else:
    shipping_cost += 5

print(f"Shipping cost: {shipping_cost}")