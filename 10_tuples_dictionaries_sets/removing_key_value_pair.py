# To avoid getting an error when removing a key, its good practice to first use a "in" keyword to check if the key exist.


ticket = {"seat no.": 25, "window": True}
ticket.pop("window")
print(ticket)


ticket = {"seat no.": 25, "window": True}
if "destination" in ticket:                 # To avoid getting an error when removing a key use "in" keyword.
    ticket.pop("destination")
print(ticket)


participants = {"Edin": True, "Andrina": True, "Edina": False}
andrina = participants.pop("Andrina")
print(andrina)


crypto = {"BTC": True, "ETH": True, "LUNA": False}
if "XRP" in crypto:                         # avoid getting an error by if statemant before removing.
    crypto.pop("XRP")