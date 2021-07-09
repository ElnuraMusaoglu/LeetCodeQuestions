'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Example 2:

Input: s = "IV"
Output: 4
Example 3:

Input: s = "IX"
Output: 9
Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

Runtime: 56 ms, faster than 26.70% of Python3 online submissions for Roman to Integer.
Memory Usage: 14.2 MB, less than 56.32% of Python3 online submissions for Roman to Integer.

'''

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dic_2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        count = 0
        while count < len(s):
            if s[count:count+2] in dic_2 and count < len(s) - 1:  # check for last index
                result += dic_2[s[count:count+2]]
                count += 2
            else:
                result += dic[s[count]]
                count += 1

        return result


print(Solution().romanToInt('III'))                  # 3
print(Solution().romanToInt('IV'))                   # 4
print(Solution().romanToInt('IX'))                   # 9
print(Solution().romanToInt('LVIII'))                # 58
print(Solution().romanToInt('MCMXCIV'))              # 1994
