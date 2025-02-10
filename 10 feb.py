class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        digits = "0123456789"
        marked = set()  
        stack = []  
        for i, j in enumerate(s):
            if j in digits:  
                if stack: 
                    marked.add(stack.pop())  
                marked.add(i) 
            else:
                stack.append(i) 
        return s if not marked else ''.join(s[i] for i in range(len(s)) if i not in marked)

