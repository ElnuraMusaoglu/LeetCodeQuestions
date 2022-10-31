'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

Runtime: 52 ms, faster than 46.38% of Python3 online submissions for Search Insert Position.
Memory Usage: 15.1 MB, less than 52.45% of Python3 online submissions for Search Insert Position.
'''
from typing import List


class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = int(len(nums)) - 1

        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:  # Search in left side
                right = middle - 1
            else:  # Search in right side
                left = middle + 1
        return left

    def searchInsert2(self, nums: List[int], target: int) -> int:
        # check for constraint first and last situation
        if len(nums) == 0:
            return 0
        if target > nums[int(len(nums))-1]:
            return int(len(nums))
        if len(nums) == 1:
            return 0 if target <= nums[0] else 1

        mid = int(len(nums) / 2)
        if target >= nums[mid]:
            start = mid
            finish = int(len(nums))
        else:
            start = 0
            finish = mid

        for i in range(start, finish):
            if nums[i] >= target:
                return i
            else:
                result = finish

        return result


print(Solution().searchInsert([1, 3], 2))                 # 1
print(Solution().searchInsert([1, 3], 1))                 # 0
print(Solution().searchInsert([1, 3, 5, 6], 5))           # 2
print(Solution().searchInsert([1, 3, 5, 6], 2))           # 1
print(Solution().searchInsert([1, 3, 5], 4))              # 2
print(Solution().searchInsert([1, 3, 5, 6], 7))           # 4
print(Solution().searchInsert([1, 3, 5, 6], 0))           # 0
print(Solution().searchInsert([1], 0))                    # 0
print(Solution().searchInsert([1], 2))                    # 1
