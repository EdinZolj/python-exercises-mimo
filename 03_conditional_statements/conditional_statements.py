# Software doesnt just decide what to do when a condition is True, it also has a back-up plan if the condition is False.
# When moving a "slider", this program uses conditional statement to show different greetings if the hour is less than 7, 12, 17, and 21.

hour = 18

if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")
else:
    print("Good night")