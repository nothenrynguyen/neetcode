class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # this can be similar to the previous example except instead we only use the output array

        # Example:
        # nums = [1, 2, 4, 6]

        # we build the output array with each prefix 1 index to the right, defaulting at 1
        # and we store the prefix product as we go along
        # output = [1, 1, 2, 8]

        # then we go thru the array and do the postfix backwards,
        # so there's no postfix for the last spot so that defaults to 1,
        # and 1 x 8 keeps the output in the last index at 8,
        # then we multiple the postfix to the right reverse from how we did prefix
        
        # so next is 1x6 which is 6 and we store that is individual postfix int,
        # we multiple that postfix val to the index at 2 to get 12, and move on

        # again, postfix x the val left is 6 x 4 = 24 which we mult to the 1 in index 1 = 24
        # and last, postfix is 24 x the next left so 24 x 2 = 48 multipled to index 0 val 1 is 48

        result = [1] * len(nums) # creates a result output array

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] = result[i] * postfix
            postfix = postfix * nums[i]

        return result
        
        # and this is still O(n) time but its better on space cuz we only make an output array
        # or O(1) in this case cuz the problem says output doesnt count


        
        