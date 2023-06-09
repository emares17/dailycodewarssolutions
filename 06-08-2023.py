# LeetCode 914. X of a Kind in a Deck of Cards

# You are given an integer array deck where deck[i] represents the number written on the ith card.

# Partition the cards into one or more groups such that:

# Each group has exactly x cards where x > 1, and
# All the cards in one group have the same integer written on them.
# Return true if such partition is possible, or false otherwise.

 

# Example 1:

# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
# Example 2:

# Input: deck = [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.

# -------------------------------Solution----------------------------------

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count  = collections.Counter(deck)
        val = count.values()
        
        import math
        
        m = math.gcd(*val)
        
        if m >= 2:
            return True
        
        return False