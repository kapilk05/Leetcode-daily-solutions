from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans, t_inc, t_dec = 1, 1, 1
        for q in range(1, len(nums)):
            p = q - 1 
            
            if nums[q] > nums[p]:  
                t_inc += 1
                t_dec = 1 
            elif nums[q] < nums[p]: 
                t_dec += 1
                t_inc = 1 
            else: 
                t_inc = t_dec = 1
            
            ans = max(ans, t_inc, t_dec)
        
        return ans
