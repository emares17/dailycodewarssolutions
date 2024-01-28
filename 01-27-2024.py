# LeetCode 1346. Check If N and Its Double Exist

# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
 

# Example 1:

# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
# Example 2:

# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.

# -------------------------------------Solution-------------------------------------

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        
        for i in range(len(arr)):
            total = arr[i] * 2
            l, r = 0, len(arr) - 1
        
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == total and mid != i:
                    return True
                elif arr[mid] < total:
                    l += 1
                else:
                    r -= 1
                    
        return False