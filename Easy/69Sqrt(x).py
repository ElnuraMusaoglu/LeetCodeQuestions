class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        if x < 4: return 1
        smaller, bigger, i = 0, 1, 2
        while x >= smaller:
            smaller = bigger
            bigger = i * i
            if bigger == x:
                return i
            if smaller<= x and bigger>= x:
                return i-1
            i=i+1


print(Solution().mySqrt(x=5))
print(Solution().mySqrt(x=1))
print(Solution().mySqrt(x=8))
print(Solution().mySqrt(x=9))
print(Solution().mySqrt(x=16))
print(Solution().mySqrt(x=26))
print(Solution().mySqrt(x=2147395599))
