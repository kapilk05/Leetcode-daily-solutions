class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                prod = nums[i] * nums[j]
                d[prod] += 1
        count = 0
        for i in d.values():
            if i > 1:
                count += 8 * (i * (i - 1) // 2) 

        return count
