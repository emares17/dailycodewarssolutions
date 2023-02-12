# Crash Override

# Every budding hacker needs an alias! The Phantom Phreak, Acid Burn, Zero Cool and Crash Override are some notable 
# examples from the film Hackers.

# Your task is to create a function that, given a proper first and last name, will return the correct alias.

# Notes:
# Two objects that return a one word name in response to the first letter of the first name and one for the first letter 
# of the surname are already given. See the examples below for further details.

# If the first character of either of the names given to the function is not a letter from A - Z, you should return 
# "Your name must start with a letter from A - Z."

# Sometimes people might forget to capitalize the first letter of their name so your function should accommodate for 
# these grammatical errors.

# Examples
# # These two dictionaries are preloaded, you need to use them in your code
# FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', ...}
# SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst' ...}

# alias_gen('Larry', 'Brentwood') == 'Logic Bomb'
# alias_gen('123abc', 'Petrovic') == 'Your name must start with a letter from A - Z.'

# -----------------------------Solution-------------------------------

def alias_gen(f_name, l_name):
    first_initial = f_name[0].upper()
    last_initial = l_name[0].upper()
    
    if not first_initial.isalpha() or not last_initial.isalpha():
        return "Your name must start with a letter from A - Z."
    
    first_word = FIRST_NAME.get(first_initial, " ")
    last_word = SURNAME.get(last_initial, " ")
    
    if first_word == " " or last_word == " ":
        return "Your name must start with a letter from A - Z."
    
    return f"{first_word} {last_word}"
