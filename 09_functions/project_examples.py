# Morse Encoder - Program converts a set of numbers to morse code.
# We will replace each number of the passed code parameter with its morse correspondent and return the result.
# Replace returns the original string if the string to be replaced isnt found.

from xml.sax.handler import feature_namespace_prefixes


def convert_to_morse(code):

    code = code.replace("1", ".----")
    code = code.replace("2", "..---")
    code = code.replace("3", "...--")
    code = code.replace("4", "....-")
    code = code.replace("5", ".....")
    code = code.replace("6", "-....")
    code = code.replace("7", "--...")
    code = code.replace("8", "---..")
    code = code.replace("9", "----.")
    code = code.replace("0", "-----")

    return code

lock_code = "1 2 2 5 0"
print(f"Initiatil code: {lock_code}")

morse = convert_to_morse(lock_code)
print(f"Morse code: {morse}")


# Fare split calculator - Program uses multiple paramenter to create a funtion that splits a Doober fare between several users.
# We will divide the price by the number of passengers first. Then, well add a smal feature cost to each passengers share.

def split_fare(fare, passengers, feature_cost):

    share = fare/passengers
    print(f"Splitting the € {fare} fare between {passengers} passengers...")

    shared_cost = share + feature_cost
    print(f"Adding a € {feature_cost} feature cost...")
    return shared_cost

fare_cost = 36
passengers = 3
feature_cost = 0.5

shared_cost = split_fare(fare_cost, passengers, feature_cost)

print(f"Each pays: € {shared_cost}")
