class Solution(object):
    def constructDistancedSequence(self, n):
        size = 2 * n - 1
        result = [0] * size
        used = set()

        def backtrack(pos):
            if pos == size:
                return True
            if result[pos] != 0:
                return backtrack(pos + 1)

            for i in range(n, 0, -1):
                if i in used:
                    continue
                if i == 1:
                    result[pos] = 1
                    used.add(1)
                    if backtrack(pos + 1):
                        return True
                    result[pos] = 0
                    used.remove(1)
                else:
                    if pos + i < size and result[pos] == 0 and result[pos + i] == 0:
                        result[pos], result[pos + i] = i, i
                        used.add(i)
                        if backtrack(pos + 1):
                            return True
                        result[pos], result[pos + i] = 0, 0
                        used.remove(i)
            return False

        backtrack(0)
        return result

