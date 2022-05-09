# We pass lists to function just like we do any other value.
# Paratemers are like variables storing the value we pass to a function.
# Inside the function, we can use the list operations, like len(), etc..

def display_programs(movies):
    print(f"Airing tonight: {movies}")

movie_list = ["Alien", "Moon"]
display_programs(movie_list)


def count_passengers(passengers):
    print(len(passengers))

passengers = ["June", "Sam", "Lee"]
count_passengers(passengers)


def get_winner