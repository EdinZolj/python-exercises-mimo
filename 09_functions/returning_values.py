# Function can return a value to the code that called it. 
# To return something from a function we add the return keyword followed by the value to return.
# A function can return any type of value.
# Both return and display statements are considered outputs.

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


def sign_up(user):
    status = user + " signed up"
    return status

print(sign_up("Edin"))


def get_area(height):
    width = 26;
    return width * height

print(f"Rectangle area: {get_area(100)}")


def add_ten(number):
    result = 10 + number
    return result

print(f"Result: {add_ten(20)}")


def reject_cookies(user):
    user + ": No Cookies";      # By forgeting to add the return statement, we will return a "None"    

print(reject_cookies ("Erica"))


def get_email(name, year, domain):
    return name + year + domain

email = get_email("Edin", "1979", "@hotmail.com")
print(email)