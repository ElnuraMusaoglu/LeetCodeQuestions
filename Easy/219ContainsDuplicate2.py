import  pytest

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        nums_dic = {}
        for i, num in enumerate(nums):
            if num in nums_dic:
                if i - nums_dic[num] <= k:
                    return True
            nums_dic[num]=i
        return False

print(Solution().containsNearbyDuplicate([1,2,3,1], 3))
print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2))

