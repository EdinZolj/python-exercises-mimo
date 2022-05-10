#  function can return a value to the code that called it. 
# To return something from a function we add the return keyword followed by the value to return.
# A function can return any type of value.

def age_label(age):
    lable = "User age: " + age
    return lable                    #if we dont include a return statement, the function returns the value None instead.

result = age_label("29")            #we can store the return value in a variale too.
print(result)


def add_greeting(user):
    greeting = "Greetings " + user
    return greeting

result = add_greeting("Simon")
print(result)


def sign_up(user):
    status = user + " signed up"
    return status

result = sign_up("Desmond")
print(result)


def get_area(height):
    width = 26;
    return width * height

print(f"Rectangle area: {get_area(100)}")