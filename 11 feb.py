class Solution:
    def calculateLPS(self, part: str, n: int, lps: list):
        i, j = 0, 1

        while j < n:
            if part[i] == part[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            else:
                if i > 0:
                    i = lps[i - 1]
                else:
                    j += 1

    def removeSubstrings(self, s: str, part: str, lps: list):
        m, n = len(s), len(part)
        i, j = 0, 0  # i for s, j for part

        while i < m:
            if s[i] == part[j]:
                i += 1
                j += 1
            
            if j == n:  # Found a match
                s = s[:i - n] + s[i:]  # Remove substring
                m = len(s)  # Update size of string
                i = max(0, i - 2 * n)  # Update start point
                j = 0
            
            if i < m and s[i] != part[j]:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]

        return s

    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        lps = [0] * n
        
        self.calculateLPS(part, n, lps)
        return self.removeSubstrings(s, part, lps)
