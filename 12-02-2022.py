# Absent vowel

# Your job is to figure out the index of which vowel is missing from a given string:

# A has an index of 0,
# E has an index of 1,
# I has an index of 2,
# O has an index of 3,
# U has an index of 4.
# Notes: There is no need for string validation and every sentence given will contain all vowels but one. Also, 
# you won't need to worry about capitals.

# Examples
# "John Doe hs seven red pples under his bsket"          =>  0  ; missing: "a"
# "Bb Smith sent us six neatly arranged range bicycles"  =>  3  ; missing: "o"

# --------------------------------Solution--------------------------------

def absent_vowel(x): 
    stack = []
    vowels = 'aeiou'
    for i in x:
        if i in vowels:
            stack.append(i)
    for i in vowels:
        if i not in stack:
            return vowels.index(i)

# ------------------------------------Or----------------------------------

def absent_vowel(x): 
    vowels = 'aeiou'
    for i in vowels:
        if i not in x:
            return vowels.index(i)