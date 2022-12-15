# Highest Scoring Word

# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

# ------------------------Solution--------------------------

def high(x):
    sentence = x.split()
    high_score = []
    for word in sentence:
        total = 0
        letters = list(word)
        for letter in letters:
            total += ord(letter) - 96
        high_score.append(total)
    return sentence[high_score.index(max(high_score))]