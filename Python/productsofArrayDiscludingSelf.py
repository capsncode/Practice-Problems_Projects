# Products of Array Discluding Self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in O(n) time without using the division operation?

# Example 1:
# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]

# Example 2:
# Input: nums = [-1,0,1,2,3]
# Output: [0,-6,0,0,0]

# Constraints:
# 2 <= nums.length <= 1000
# -20 <= nums[i] <= 20
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        left = 1
        for i in range(n):
            output[i] =  left
            left *= nums[i]
        
        right = 1
        for i in range (n - 1, -1, -1):
            output[i] *=right
            right *= nums[i]

        return output