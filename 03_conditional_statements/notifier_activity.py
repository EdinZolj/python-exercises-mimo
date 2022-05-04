#Program notifies a user about the last activity on their social media.

action = "reply"

if action == "like":
    print("Someone has liked your post")
elif action == "comment":
    print("Someone has commented on your post")
elif action == "reply":
    print("Someone has replied to your post")
else:
    print("There is activity on your page")