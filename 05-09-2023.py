# LeetCode 1437. Check If All 1's Are at Least Length K Places Away

# Given an binary array nums and an integer k, return true if all 1's are at least k places 
# away from each other, otherwise return false.

 

# Example 1:


# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# Explanation: Each of the 1s are at least 2 places away from each other.
# Example 2:


# Input: nums = [1,0,0,1,0,1], k = 2
# Output: false
# Explanation: The second 1 and third 1 are only one apart from each other.

# ---------------------------Solution------------------------------

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        l = -1
        for r in range(len(nums)):
            if nums[r] == 1:
                if l != -1 and r - l - 1 < k:
                    return False
                l = r
        return True