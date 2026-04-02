class Solution:
    def findMin(self, nums: List[int]) -> int:

        result = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:

            # if we get to a subarray that is alr sorted
            # then we can potentially update our result
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
        
            # if the array is not sorted
            # ( this is the main part of the problem )
            # binary search

            mid = (left + right) // 2
            result = min(result, nums[mid])

            # checking if the mid value is part of
            # the left or right sorted portion
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return result
