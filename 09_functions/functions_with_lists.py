# We pass lists to function just like we do any other value.
# Paratemers are like variables storing the value we pass to a function.
# Inside the function, we can use the list operations, like len(), etc..

from unicodedata import name


def display_programs(movies):
    print(f"Airing tonight: {movies}")

movie_list = ["Alien", "Moon"]
display_programs(movie_list)


def count_passengers(passengers):
    print(len(passengers))

passengers = ["June", "Sam", "Lee"]
count_passengers(passengers)


def get_winner(top_players):
    winner = top_players[0]
    print(f"Game winner: {winner}")

top_players = ["Jay", "Meg", "Cy"]
get_winner(top_players)


def update_first_place(leaderboard, player):
    leaderboard[0] = player
    return leaderboard

leaderboard = ["Jay", "Meg", "Cy"]
leaderboard = update_first_place(leaderboard, "Lena")
print(leaderboard)


def set_initials(names, initial):   # it updates the name at index 0 to its initial
    names[0] = initial
    print(names)

author_names = ["Francis", "Scott", "Firtzgerald"]
set_initials(author_names, "F.")


def update_first_place(leaderboard, player):
    leaderboard[0] = player
    return leaderboard

leaderboard = ["Jay", "Meg", "Cy"]
leaderboard = update_first_place(leaderboard, "Lena")
print(leaderboard)


def has_two_for_one(basket):    # Check if the user qualifies for a two-for-one discount by checking if the length of basket is at least 2.
    print(len(basket) >= 2)

basket_items = ["t-shirts", "jeans", "jeans"]
has_two_for_one(basket_items)


def show_schedule(courses):
    print(f"Monday: {courses[0]}")
    print(f"Tuesday: {courses[1]}")
    print(f"Thrusday: {courses[2]}")

courses = ["Algebra", "Statistics", "Machine Learning"]
show_schedule(courses)