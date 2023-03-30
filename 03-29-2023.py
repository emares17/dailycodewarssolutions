# LeetCode 1832. Check if the Sentence Is Pangram

# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, 
# or false otherwise.

 

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false

# -------------------------Solution-----------------------------

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashmap = {}
        alphabet_string = "abcdefghijklmnopqrstuvwxyz"

        for letter in sentence:
            hashmap[letter] = hashmap.get(letter, 0) + 1
        
        for letter in alphabet_string:
                if letter not in hashmap:
                    return False
        return True