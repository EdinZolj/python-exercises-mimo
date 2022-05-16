# We can store tuples in a list like any other value.
# We consider each tuple to be one value/element.
# The main differences is that unlike lists, we can not update, add or delete values from tuples.
# We say tuples are immutable, we use them to store information that shouldn't be modified, like a persons name and birth date.

score = [("mia", 75), ("lee", 90)]
print(score)

score = [("mia", 75), ("lee", 90)]
print(len(score))


score = [("mia", 75), ("lee", 90)]
mia_score = score[0]
print(mia_score)


score = [("mia", 75), ("lee", 90)]
for user_score in score:
    print(f"Result: {user_score}")


event_tuple = ("Saturday", "21:00", "Annas Bday")


