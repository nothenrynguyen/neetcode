class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # we can't use a hashset cuz problem requires constant space

        # this is linked list cycle + floyd's algo
        # idk how we'd figure this out on our own

        # range is 1 to n so if we point value to index, we'll never point to index 0
        # and we look for a loop

        # yea ts is cooked lmaooo

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow
            