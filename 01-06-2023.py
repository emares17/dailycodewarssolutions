# Count consonants

# Write a function consonantCount, consonant_count or ConsonantCount that takes a string of English-language text 
# and returns the number of consonants in the string.

# Consonants are all letters used to write English excluding the vowels a, e, i, o, u.

# ------------------------------Solution--------------------------------

def consonant_count(s):
    count = 0
    constants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    for words in s.lower():
        for letter in words:
            if letter in constants:
                count += 1
    return count