'''

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0


Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-10**4 <= target <= 10**4

'''

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = nums[l] + nums[r] + nums[i]
                if curSum == target:
                    return target
                if abs(curSum-target) < abs(result-target):
                    result = curSum
                if curSum < target:
                    l += 1
                else:
                    r -= 1
        return result

print(Solution().getMoneyAmount([-1,2,1,-4], 1))

