#Program that keeps track of a personal's savings and updates if the person has made purchases or earned money.

goal = 150
savings = 70

print(f"Your're €{goal - savings} away from your goal")

earned = 75
savings += earned

print(f"You're €{goal - savings} away from your goal")

spent = 25
savings -= spent

print(f"You're €{goal - savings} away from your goal")