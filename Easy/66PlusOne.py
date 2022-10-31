class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 1
        for i in range(len(digits)-1, -1, -1):
            sum = digits[i] + sum
            digits[i] = sum%10
            sum = sum//10
        if sum > 0:
            digits.append(1)
            return digits[::-1]
            
        return digits
            
            

print(Solution().plusOne([9,9,9]))
print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([1,2,9]))
print(Solution().plusOne([1,9,9]))
      