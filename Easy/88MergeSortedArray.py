import sys


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m < 1:
            nums1[:] = nums2[:n]
        elif n <1:
            nums1[:] = nums1[:m]
        else:
            nums1[:] = sorted(nums1[:m] + nums2[:n])

m1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
0
m2=[-50,-50,-48,-47,-44,-44,-37,-35,-35,-32,-32,-31,-29,-29,-28,-26,-24,-23,-23,-21,-20,-19,-17,-15,-14,-12,-12,-11,-10,-9,-8,-5,-2,-2,1,1,3,4,4,7,7,7,9,10,11,12,14,16,17,18,21,21,24,31,33,34,35,36,41,41,46,48,48]
63
print(Solution().merge(m1, 0, m2, 63))
print(Solution().merge([1,2,4,5,6,0], 5, [3], 1))
print(Solution().merge([2,0], 1, [1], 1))
print(Solution().merge([0], 0, [1], 1))
print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(Solution().merge([1], 1, [], 0))

