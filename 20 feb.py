class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        return "".join("0" if nums[i][i] == "1" else "1" for i in range(len(nums)))

        
