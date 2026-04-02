class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # remember that sorting an array is O(nlogn)

        result = []
        nums.sort()

        for i, a in enumerate(nums):        # enumerate cuz we want index & value
            if i > 0 and a == nums[i-1]:    # checks if the value is the same as previous
                continue                    # cuz we don't want duplicates

            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:                # if sum is greater than target 0
                    right = right - 1
                elif threeSum < 0:              # if sum is less than target 0
                    left = left + 1
                else:
                    result.append([a, nums[left], nums[right]])

                    left = left + 1
                    # means if the next value is the same
                    while nums[left] == nums[left - 1] and left < right: 
                        left = left + 1

                        # we only need to change 1 pointer ( here we do left )
                        # cuz the logic above will always adapt to if we are greater/less than 0

        return result

        # so time is O(nlogn) + O(n^2) which reduces to just O(n^2)
        # space is either O(1) or O(n) cuz sorting may take space in some libraries
        # -> just good to know in case it's asked
        