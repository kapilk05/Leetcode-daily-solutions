class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        def dfs(n):
            count = 0
            for char in n:
                if n[char] > 0:
                    count += 1
                    n[char] -= 1
                    count += dfs(n)
                    n[char] += 1
            return count

        return dfs(Counter(tiles))
