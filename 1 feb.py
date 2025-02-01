class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        isSpecial = True
        n = len(nums)
        for i in range (n-1):
            if (nums[i] % 2 == 0  and nums[i+1] % 2 == 0) or (nums[i] % 2 != 0  and nums[i+1] % 2 != 0):
                isSpecial = False
        return isSpecial
