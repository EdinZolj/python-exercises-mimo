# Type function "type()"
# Sometimes we need to change values from one type to another.

from re import sub


print(type("hello"))
print(type(10.5))
print(type(10))
print(type(True))

#int() function

price = 9.99
print(int(price))

#equivalent numerical value for booleans are "1 for True" and "0 for False".

member = True       
value = int(member)
print(value)

#Python also provides the list(), dict(), set(), tuple(), funtions for "type conversions"

user_1 = [1, "Sara"]
user_2 = [2, "Andy"]

data = dict([user_1, user_2])
print(data)

#A club has a membership sign-up from where the data arrives as strings.

name_box = "Alice Bentall"
age_box = "20"
uni_box = ""
sub_box = "1.99"
mkt_box = "0"

name_entered = bool(name_box)   #When using with a string, the "bool()" function will return "True" if the string is non-empty, oherwise "False"
if name_entered:
    name = name_box
else:
    name = "Unknown"

age = int(age_box)
student = bool(uni_box)
subscription = float(sub_box)
marketing = bool(int(mkt_box))

profile = name + ", " + str(age)
print(profile)
print(student)
print(subscription)
print(marketing)