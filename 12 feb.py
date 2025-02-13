class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sum_of_digits(n):
            return sum(int(d) for d in str(n))  

        digit_sum_map = {}
        max_sum = -1  

        for num in nums:
            a = sum_of_digits(num)

            if a in digit_sum_map:
                max_sum = max(max_sum, num + digit_sum_map[a])

            digit_sum_map[a] = max(digit_sum_map.get(a, 0), num)

        return max_sum
