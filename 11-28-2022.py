# Number Of Occurrences

# Write a function that returns the number of occurrences of an element in an array.

# Examples
# sample = [0, 1, 2, 2, 3]
# number_of_occurrences(0, sample) == 1
# number_of_occurrences(4, sample) == 0
# number_of_occurrences(2, sample) == 2
# number_of_occurrences(3, sample) == 1

# -----------------------------Solution-------------------------------

def number_of_occurrences(element, sample):
    count = 0 
    for i in sample:
        if i == element:
            count += 1
    return count

# ----------------------------Or-------------------------------------

def number_of_occurrences(element, sample):
    return sample.count(element)