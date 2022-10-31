class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) < 1: return 0
        uniqueCount = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[uniqueCount] = nums[i] 
                uniqueCount = uniqueCount+1
                
        return uniqueCount

       
Solution().removeDuplicates([1,1,2])
