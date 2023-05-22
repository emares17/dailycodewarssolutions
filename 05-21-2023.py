# LeetCode 1287. Element Appearing More Than 25% In Sorted Array

# Given an integer array sorted in non-decreasing order, there is exactly one integer 
# in the array that occurs more than 25% of the time, return that integer.

 

# Example 1:

# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
# Example 2:

# Input: arr = [1,1]
# Output: 1

# -----------------------------Solution---------------------------------

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr) / 4
        dicti = {}
        for i in arr:
            dicti[i] = dicti.get(i, 0) + 1
            
        for k,v in dicti.items():
            if v > quarter:
                return k