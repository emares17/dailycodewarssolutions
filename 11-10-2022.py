# Changing letters

# When provided with a String, capitalize all vowels

# For example:

# Input : "Hello World!"

# Output : "HEllO WOrld!"

# Note: Y is not a vowel in this kata.

# -----------------------------Solution-------------------------------

def swap(st):
    capital = ''
    for letter in st:
        if letter not in 'aeiou':
            capital = capital + letter
        else:
            capital = capital + letter.upper()
    return capital