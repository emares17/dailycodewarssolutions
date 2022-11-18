# Find the capitals

# Instructions
# Write a function that takes a single string (word) as argument. The function must return an ordered list containing 
# the indexes of all capital letters in the string.

# Example
# Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );

# -------------------------------Solution----------------------------------

def capitals(word):
    stack = []
    for i, c in enumerate(word):
        if c.isupper():
            stack.append(i)
    return stack