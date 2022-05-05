#How many times a pice of data is present, such as the most frequent answer to a survey.

answer = ["yes", "no", "sometimes", "yes"]
print("for yes: " + str(answer.count("yes")))
print("for no: " + str(answer.count("no")))
print("for sometimes: " + str(answer.count("sometimes")))

#We can use any type of value, like checking how many free seats are left in a row by the number of True values.

free_seats = [False, False, True, True, False]
print("Number of free Seats: " + str(free_seats.count(True)))
print(f"Number of free Seats: {free_seats.count(True)}")

#if we dont know the exact number, but only if an element like "suger" exists, we use the "in" keyword.

ingredients = ["flour", "butter", "sugar", "eggs"]
#print("sugar" in ingredients)

has_sugar = "sugar" in ingredients
print("Ingredients has sugar: " + str(has_sugar))

#Analyze collection of product ratings, by counting how many one and five-star ratings are and display them.

ratings = [5, 5, 3, 1, 1, 1, 4, 5, 3, 5]

five_star = ratings.count(5)
one_star = ratings.count(1)

amounts = [five_star, one_star]

print("Five star rating:")
print(amounts[0])

print("One star rating:")
print(amounts[1])