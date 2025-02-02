class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        count = 0 
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count+=1
        return False if count > 1 else True
