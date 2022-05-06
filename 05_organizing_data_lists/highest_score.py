# Code that helps an arcade machine find the highest score from a list of scores.

user_score = [12, 42, 55, 100, 11, 22]
highest = user_score[0]

for score in user_score:
    if score > highest:
        highest = score

print(f"Highest score: {highest}")