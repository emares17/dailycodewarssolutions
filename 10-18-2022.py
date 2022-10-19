# esreveR

# Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)

# (the dedicated builtin(s) functionalities are deactivated)

# --------------------------------Solution----------------------------------

def reverse(lst):
    out = list()
    for x in lst:
        out.insert(0, x)
    return out