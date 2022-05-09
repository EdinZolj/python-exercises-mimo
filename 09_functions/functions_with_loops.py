# Functions help us reuse loops by allowing us to change the number of repetitions or the list we're iterating through.
# We can use both while and for loops inside functions.

def onboard_passengers(bookings):
    counter = 1 
    while counter <= bookings:
        print(f"Passengers {counter} on board")
        counter += 1

onboard_passengers(4)


def do_countdown(counter):
    while counter > 0:
        print(counter)
        counter -= 1
    print("Go!")

do_countdown(3)


def display_progress():
    for i in range(3):                              # Ranges like range(3) tell us how many times the for loop runs.
        print(f"Downloading file {i} out of 3")

display_progress()


def display_progress(total_files):
    for i in range(total_files):                     # to reuse a for loop with any range, we pass a parameter, between the parentheses of range().
        print(f"Downloading file {i} out of {total_files}")

display_progress(3)


def show_progress(total):
    for i in range(total):
        print("Installing next update")

show_progress(3)


def halve_price(cart):
    for price in cart:                                # to reuse a loop that interetes through a list, we nest it in a function.
        print(f"New price: {price/2}")

cart_list = [5, 20, 8]
halve_price(cart_list)


def show_next_track():
    playlist = ["Hey Jude", "Helter Skelter", "Something"]
    for track in playlist:
        print(f"Next up: {track}")

show_next_track()