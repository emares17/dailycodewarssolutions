# Simple Fun #176: Reverse Letter

# Task
# Given a string str, reverse it and omit all non-alphabetic characters.

# Example
# For str = "krishan", the output should be "nahsirk".

# For str = "ultr53o?n", the output should be "nortlu".

# Input/Output
# [input] string str
# A string consists of lowercase latin letters, digits and symbols.

# [output] a string

# -------------------------------Solution--------------------------------

def reverse_letter(string):
    stack = []
    for letter in list(string):
        if letter.isalpha():
            stack.append(letter)
    return ''.join(stack)[::-1]