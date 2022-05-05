#Sorted lists are usful when we want to unterstand where individual datapoints, such as scores, stand in relation to the others.

score = [3, 6, 1, 12]
score.sort()
print(score)

#Sort a list of customers and assign them to the first available customer service desks.

customers = ["Filip", "Miranda", "Ariah", "Laurence", "Shahid"]
free_counters = [11, 20, 14, 6, 4]

customers.sort()        #sort alphabetically to decide who goes first.
free_counters.sort()

customer = customers[0]
counter = free_counters[0]

print(customer)
print("Visit counter:")
print(counter)