"""
485. Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's in the array.


Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MaxConsect = 0
        CurrConsect = 0
        
        for num in nums:
            
            if num == 1:
                CurrConsect += 1
                if CurrConsect > MaxConsect:
                    MaxConsect = CurrConsect
                    
            if num == 0:
                CurrConsect = 0
        
        return MaxConsect
