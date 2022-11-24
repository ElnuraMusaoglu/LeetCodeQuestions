class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dic = {}
        
        for num in nums:
            if num in nums_dic:
                nums_dic[num]+=1
            else:
                nums_dic[num]=1
        for k,v in nums_dic.items():
            if v > 1:
                return True
        
        return False