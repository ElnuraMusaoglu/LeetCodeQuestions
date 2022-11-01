class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return n
        p1, p2 = 1, 2
        result = p1+p2
        for _ in range(3, n+1):
            result = p1+p2
            p1=p2
            p2=result
        
        return result


print(Solution().climbStairs(5))
