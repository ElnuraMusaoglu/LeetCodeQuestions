'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.


Runtime: 56 ms, faster than 84.24% of Python3 online submissions
Memory Usage: 14.5 MB, less than 23.50% of Python3 online submissions

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_unrepeated_count = 0
        substring_map = {}
        start_idx = 0
        for i in range(len(s)):
            position = substring_map.get(s[i])
            if position is not None and position >= start_idx:
                length = i - start_idx
                start_idx = position + 1
                max_unrepeated_count = max(length, max_unrepeated_count)
            substring_map[s[i]] = i

        return max(len(s) - start_idx, max_unrepeated_count)




result = Solution().lengthOfLongestSubstring("abcabcbb")
"abcabcbb"
"bbbbb"
"pwwkew"
" "
""
if result == 3:
    print('Succeed')
else:
    print('Fail')
