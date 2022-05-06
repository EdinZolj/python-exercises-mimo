# Program checks if a data point is within the appropriate range for the given dataset.

low = 55
high = 135
point = 67

if point > high:
    print("Data point is too high")
elif point < low:
    print("Data point is too low")
else:
    print("Valid data point")