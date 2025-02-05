class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        not_equal = 0
        res = dict()
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                not_equal += 1
                res[i] = (s1[i], s2[i])
        if not_equal == 0:
            return True 
        elif not_equal == 2:
            (i, j) = res.keys()
            return res[i] == res[j][::-1]
        else:
            return False 
        
