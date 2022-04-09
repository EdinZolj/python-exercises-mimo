#Keeping track of our followers. Program will alert us when we reach one million or let us know how many we have left.

followers = 999991
one_mil = 1000000

if followers >= one_mil:
    print("You have one million followers!")
else:
    followers_left = one_mil - followers
    print(f"You're {followers_left} away from one million.")