# LeetCode 409. Longest Palindrome

# Given a string s which consists of lowercase or uppercase letters, return the length of the 
# longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

# --------------------------------Solution-------------------------------------

class Solution:
    def longestPalindrome(self, s: str) -> int:
        dicti = {}
        for letter in s:
            dicti[letter] = dicti.get(letter, 0) + 1
            
        count = 0
        odd =  False
        for v in dicti.values():
            if v % 2 == 0:
                count += v
            else:
                odd = True
                count += v - 1
        
        return count + int(odd)