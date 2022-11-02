# Vowel one

# vowelOne
# Write a function that takes a string and outputs a strings of 1's and 0's where vowels become 1's and non-vowels become 0's.

# All non-vowels including non alpha characters (spaces,commas etc.) should be included.

# Examples:

# vowelOne "abceios" -- "1001110"

# vowelOne "aeiou, abc" -- "1111100100"

# -------------------------------Solution--------------------------------

def vowel_one(s):
    vowels = "AEIOUaeiou"
    stack = []
    for i in s:
        if i in vowels:
            stack.append('1')
        else:
            stack.append('0')
    return ''.join(stack)
