#App keep track of tennis games until it reaches a set of 6 games.

games = 0
set_finished = False

while set_finished == False:
    games += 1
    print(f"Games played: {games}")
    if games == 6:
        set_finished = True
print("Finished the set!")