#Using if, elif and else conditions to calculate a rideshare fare depending on the chosen ride type.
#Here in this example: How much a "Uber user" pays for a ride.

ride_type = "Black"
credits = 4

ride_price = 0
final_price = 0

if ride_type == "UberX":
    ride_price = 20.5
elif ride_type == "Black":
    ride_price = 37.9
else:
    ride_price = 18.7

print("Ride price:")
print(ride_price)

if credits > 0:
    final_price = ride_price - credits

print("Final price:")
print(final_price)