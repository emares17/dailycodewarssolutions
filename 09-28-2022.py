# Reverse words

# Complete the function that accepts a string parameter, and reverses each word in the string. 
# All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# --------------------------Soution-----------------------------

def reverse_words(text):
    text = text.split(' ')
    return ' '.join([i[::-1] for i in text])