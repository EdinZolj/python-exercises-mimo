# When working with different kind of data, we'll often receive it in a format that can make it hard to work with.

new_users = "Ann Jon Edin"
users_list = new_users.split()
print(users_list)

# We can specify exactly how we want to split a string by placing a separator inside the parentheses, like with "," here:

user = "Lauren,25,F,Architect"
user_1 = user.split(",")
print(user_1)

path = "getmimo.com/glossary/python"
path_list = path.split("/")
print(path_list)