class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # my understanding is we add each number to a hashmap
        # from left to right, and each time we compute the difference
        # and lookup if that difference exists in the hashmap

        prevMap = {} # mapping val : index

        for i, n in enumerate(nums): # we use this cuz we need val & index
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
        