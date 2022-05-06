# Program manage soil humidity data received from a greenhouse monitor. Using the list to track and update at over five days.

humidity_level = [87, 83, 89, 88, 87]

humidity_level.insert(0, 90)    #insert value "90" in index 0
humidity_level.pop()            #delete last value in list to keep "just 5 values in total in list"

print(humidity_level)