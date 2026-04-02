class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        result = 0
        count = 0

        for i in nums:
            if i == 0:
                count = 0
            else: 
                count += 1
                result = max(result, count)
        
        return result