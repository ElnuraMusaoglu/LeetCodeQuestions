'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0


Constraints:

-2^31 <= x <= 2^31 - 1

Runtime: 32 ms, faster than 70.53% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.2 MB, less than 71.87% of Python3 online submissions for Reverse Integer.

'''

class Solution:
    def reverse(self, x: int) -> int:
        mult = 1
        total = 0
        number = str(x * -1) if x < 0 else str(x)
        for i in range(len(number)):
            total = total + mult * int(number[i])
            mult = mult * 10

        result = total * -1 if x < 0 else total
        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result


print(Solution().reverse(123))                  # 321
print(Solution().reverse(-123))                 # -321
print(Solution().reverse(120))                  # 21
print(Solution().reverse(0))                    # 0
print(Solution().reverse(1534236469))           # 0
