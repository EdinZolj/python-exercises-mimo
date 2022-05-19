# We access dictionary values by their key, like: "dictionaryX[key]".
# We can loop through the dictonary key with a for loop.
# Assossiate a new key with a value we code an "=" followed by the value like below "ticket["window] = True".
# To check if a certain key is in a dictionery, we use the "in" keyword
# To avoid getting an error when removing a key, its good practice to first use a "in" keyword to check if the key exist.


actor_bio = {"name": "Bill Murry", "known for": ["Lost in Traslation", "Rushmore"]}
print(actor_bio["name"])


player_scores = {"ann": 13, "michael": 20, "ava:": 34}
for player in player_scores:          # the variable player stands for the keys, so we can access each keys value using player for the key name.
    print(player_scores[player])


air = {"nitrogen": "78%", "oxygen": "20%"}
print(air["oxygen"])


ticket = {"seat no.": 25}
ticket["window"] = True                 # Assossiate a new key with a value
print(ticket)


personal_data = {"name": "Mac MIller", "telephone": "0177452718"}
print("name" in personal_data)          # if a certain key is in a dictionery, we use the "in" keyword


stock = {"BTC": 23000, "ETH": 2000, "XRP": 0.5}
has_ETH = "ETH" in stock                # To avoid getting an error when removing a key use "in" keyword.
print(has_ETH)


crypto = {"BTC": True, "ETH": True, "LUNA": False}
if "XRP" in crypto:                         # avoid getting an error by if statemant before removing.
    crypto.pop("XRP")


ticket = {"seat no.": 25, "window": True}
ticket.pop("window")
print(ticket)


ticket = {"seat no.": 25, "window": True}
if "destination" in ticket:                 # To avoid getting an error when removing a key use "in" keyword.
    ticket.pop("destination")
print(ticket)


participants = {"Edin": True, "Andrina": True, "Edina": False}
andrina = participants.pop("Andrina")
print(andrina)