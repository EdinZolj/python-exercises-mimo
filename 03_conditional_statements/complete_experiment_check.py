# Program checks if an experiment is complete.

trials = 5
data_points = 160
peer_reviewed = True

if trials >= 5 and data_points > 100 and peer_reviewed:
    print("Experiment finished!")
else:
    print("There's more work to do.")