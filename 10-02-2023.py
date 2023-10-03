# LeetCode 1089. Duplicate Zeros

# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining 
# elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above 
# modifications to the input array in place and do not return anything.

 

# Example 1:

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:

# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]

# ----------------------Solution-------------------------

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l,r = 0, len(arr) - 1
        while l <= r:
            if arr[l] == 0:
                arr.insert(l + 1, 0)
                arr.pop()
                l += 1
            l += 1