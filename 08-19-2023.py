# LeetCode 680. Valid Palindrome II

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false

# -----------------------------Solution-------------------------------

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                if self.palindrome_check(s, l + 1, r):
                    return True
                elif self.palindrome_check(s, l, r - 1):
                    return True
                else:
                    return False
            l += 1
            r -= 1
        
        return True
    
    def palindrome_check(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True