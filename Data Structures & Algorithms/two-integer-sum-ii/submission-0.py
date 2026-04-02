class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # since this array is sorted, we can start with 2 pointers 1 on each side
        # if the sum is less than target, increment left pointer
        # if the summer is greater, decrement right pointer

        left = 0
        right = len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]

            if currentSum > target:
                right = right - 1

            elif currentSum < target:
                left = left + 1
            
            else:
                return [left + 1, right + 1]    
                # we do +1 here cuz the question uses 1 index not 0

        # time O(n) cuz we only have to iterate thru the array max once so n times
        # space O(1) cuz we don't create anything we just iterate thru the array