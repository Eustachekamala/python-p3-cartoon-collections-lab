def roll_call_dwarves(dwarfs):
    # this function takes a list of dwarfs and prints out their number and name
    for i in range(len(dwarfs)):
        print(f"{i+1}. {dwarfs[i]}")

def summon_captain_planet(text):
    # this function takes a list of text and returns a list of the same length
    # with each element capitalized and an exclamation mark added
    return [f"{item.capitalize()}!" for item in text]

def long_planeteer_calls(messages):
    # this function takes a list of messages and returns true if any of them are longer than 4 characters
    return any(len(message) > 4 for message in messages)

def find_the_cheese(messages):
    # this function takes a list of messages and returns the first one that is "cheddar"
    return next((message for message in messages if message == "cheddar"), None)
