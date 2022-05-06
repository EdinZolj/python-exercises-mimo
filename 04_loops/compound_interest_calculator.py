# Program that see how the amount stored in a bank acount increases over time, with a given rate by using while loop.

account = 100
interest_rate = 0.004
years = 3

print(f"Initial amount: {account}")

counter = 1
while counter <= years:
    accrued_interest = account * interest_rate  #angefallene Zinsen
    account += accrued_interest
    print(f"year {counter}: €{account}") #try printing below, but "#" this print here then.
    counter += 1
#print(f"Final year: €{account}")
