# Program that checks if a body is in a healthy range.

low = 97
high = 99
temp = 101.2

if temp <= high and temp >= low:
    print("You're in healthy range!")
if temp < low:
    print("Your temparature is low.")
if temp > high:
    print("Your temperature is high.")