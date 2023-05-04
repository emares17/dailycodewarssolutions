# LeetCode 2027. Minimum Moves to Convert String

You are given a string s consisting of n characters which are either 'X' or 'O'.

A move is defined as selecting three consecutive characters of s and converting them to 'O'. 
Note that if a move is applied to the character 'O', it will stay the same.

Return the minimum number of moves required so that all the characters of s are converted to 'O'.

 

Example 1:

Input: s = "XXX"
Output: 1
Explanation: XXX -> OOO
We select all the 3 characters and convert them in one move.
Example 2:

Input: s = "XXOX"
Output: 2
Explanation: XXOX -> OOOX -> OOOO
We select the first 3 characters in the first move, and convert them to 'O'.
Then we select the last 3 characters and convert them so that the final string contains all 'O's.
Example 3:

Input: s = "OOOO"
Output: 0
Explanation: There are no 'X's in s to convert.

# ------------------------------Solution----------------------------------

class Solution:
    def minimumMoves(self, s: str) -> int:
        i = 0
        count = 0
        n = len(s)
        while i < n:
            if s[i] == 'X':
                i += 3
                count += 1
            else:
                i += 1
        return count