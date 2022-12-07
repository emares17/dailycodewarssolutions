# Sort Arrays (Ignoring Case)

# Sort the given array of strings in alphabetical order, case insensitive. For example:

# ["Hello", "there", "I'm", "fine"]  -->  ["fine", "Hello", "I'm", "there"]
# ["C", "d", "a", "B"])              -->  ["a", "B", "C", "d"]

# -------------------------------Solution--------------------------------

def sortme(words):
    return sorted(words, key=str.casefold)