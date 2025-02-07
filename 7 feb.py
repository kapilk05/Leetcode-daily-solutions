class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        a, b = {}, {}
        res = []
        for x, y in queries:
            if x in a:
                old = a[x]
                if old in b:
                    b[old].discard(x)
                    if not b[old]:
                        del b[old]
            a[x] = y
            if y not in b:
                b[y] = set()
            b[y].add(x)

            res.append(len(b))
        return res

        
