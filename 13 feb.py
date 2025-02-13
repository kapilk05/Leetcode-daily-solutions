import heapq

class Solution(object):
    def minOperations(self, nums, k):
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)

        count = 0
        while len(min_heap) >= 2 and min_heap[0] < k:
            x = heapq.heappop(min_heap)
            y = heapq.heappop(min_heap)
            new_val = min(x, y) * 2 + max(x, y)
            heapq.heappush(min_heap, new_val)
            count += 1

        return count if min_heap[0] >= k else -1
