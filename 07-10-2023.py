# LeetCode 1013. Partition Array Into Three Parts With Equal Sum

# Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

# Formally, we can partition the array if we can find indexes 
# i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... 
#                 + arr[arr.length - 1])

 

# Example 1:

# Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# Example 2:

# Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
# Example 3:

# Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

# ------------------------------Solution--------------------------------

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        addition = sum(arr) 
        
        if addition % 3 != 0:
            return False
        
        l,r = 0, len(arr) - 1
        total, left, right = addition // 3, arr[l], arr[r]
        
        while l + 1 < r:
            print(left, right)
            if left == total and right == total:
                return True
            
            if left != total:
                l += 1
                left += arr[l]
                
            if right != total:
                r -= 1
                right += arr[r]
        
        return False