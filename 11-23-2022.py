# Reverse every other word in the string

# Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, 
# while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a 
# part of the word in this kata.

# -------------------------------------Solution------------------------------------

def reverse_alternate(s):
    return ' '.join(y[::-1] if x % 2 else y for x,y in enumerate(s.split()))