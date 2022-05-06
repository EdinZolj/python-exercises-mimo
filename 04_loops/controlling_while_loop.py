# Controlling the time a while loop repeats its code

counter = 1
while counter < 4:
    print(counter)
    counter += 1


acceleration = 1
while acceleration < 4:
    acceleration += 1
    print(acceleration)


first_counter = 0
while first_counter < 5:
    print("**********----------")
    first_counter += 1
    
secound_counter = 0
while secound_counter < 4:
    print("--------------------")
    secound_counter  += 1


counter = 1
while counter <= 3:
    print("Calculating averages")
    counter += 1


i = 1
while i < 5:
    print(i)
    i += 1

i = 0
while i < 10:
    i += 1
    print(i)

dollars = 1
while dollars < 10: 
    dollars += 1    # incrementing(erhöhen) the dollars variable inside the code block.
print(dollars)      # condition "< 10" = 9 + 1(dollars += 1) = result 10


tracker = 1
while tracker <= 2:
    tracker += 1
print(tracker)      # condition "<= 2" = 2 + 1(tracker += 1) = result 3


days = 0
value = 3
while days < 5:
    print(f"The value is €{value}.")
    value *= 2
    days += 1
print(f"Final value: €{value}.")