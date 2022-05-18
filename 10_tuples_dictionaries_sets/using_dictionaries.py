# We access dictionary values by their key, like: "dictionaryX[key]".
# We can loop through the dictonary key with a for loop.

actor_bio = {"name": "Bill Murry", "known for": ["Lost in Traslation", "Rushmore"]}
print(actor_bio["name"])


player_scores = {"ann": 13, "michael": 20, "ava:": 34}
for player in player_scores:                            # the variable player stands for the keys, so we can access each keys value using player for the key name.
    print(player_scores[player])


air = {"nitrogen": "78%", "oxygen": "20%"}
print(air["oxygen"])


