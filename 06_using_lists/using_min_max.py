# Program will analyze an unsorted dataset of the ten lagest lakes in the USA by using min / max.

size = [7340, 2117, 22300, 31700, 1679, 1014, 23000, 9910, 685]

largest = max(size)
print("Largest lake in sq mi:")
print(largest)

smallest = min(size)
print("smallest lake in sq mi:")
print(smallest)

difference = largest - smallest
print("Difference between lakes in sq mi:")
print(difference)