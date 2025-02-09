class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a =  defaultdict(int)
        good_pairs = 0 
        n = len(nums)
        tot = n * (n - 1) // 2
        for i, j in enumerate(nums):
            diff = j - i
            good_pairs+=a[diff]
            a[diff] += 1
        return tot - good_pairs
