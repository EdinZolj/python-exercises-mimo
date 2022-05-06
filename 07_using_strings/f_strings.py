#Using f-strings to code a programm that tracks an online store's orders and stocks.

stock = 74
item = "webcams"
orders = 18

print(f"{stock} {item} in stock")
print(f"{orders} customer orders")
print(f"{stock - orders} available")

#A tip calculator for the next evening out.

bill = 20
tip_percentage = 0.15
tax_percentage = 0.067

tip = bill * tip_percentage
print(f"Tip: € {tip}")

tax = bill * tax_percentage
print(f"Tax: € {tax}")

total = bill + tip + tax
print(f"Total: € {total}")

#Keep track of two players and the data they generate during a round-based game.

player_1 = "Sam"
player_2 = "Edin"
current_round = 1

print("Game on!")
print(f"Player 1: {player_1}")
print(f"Player 2: {player_2}")
print("----------------------")

print(f"Round {current_round}")
player_1_score = 10
player_2_score = 13
print(f"{player_2} wins with {player_2_score} to {player_1_score}")
print("----------------------")

print(f"Round {current_round +1}")
player_1_score = 20
player_2_score = 5
print(f"{player_1} defeats {player_2} by {player_1_score - player_2_score} points")