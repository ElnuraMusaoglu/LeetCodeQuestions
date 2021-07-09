'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.



Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false


Constraints:

-2**31 <= x <= 2**31 - 1

Runtime: 64 ms, faster than 53.66% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.1 MB, less than 75.29% of Python3 online submissions for Palindrome Number.
'''




class Solution:
    def isPalindrome(self, x: int) -> int:
        if x < -2**31 or x > 2**31 - 1:
            return False

        number_org = x
        reversed = 0
        while x > 0:
            reversed = reversed * 10 + x % 10
            x = x // 10

        if number_org == reversed:
           return True

        return False


print(Solution().isPalindrome(121))                  # 321
print(Solution().isPalindrome(-121))                 # -321
print(Solution().isPalindrome(10))                   # 21
print(Solution().isPalindrome(-101))                 # 0
