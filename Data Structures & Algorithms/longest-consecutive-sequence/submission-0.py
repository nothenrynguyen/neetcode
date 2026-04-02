class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # we can use a set for our entire array
        # and find the start of each sequence by seeing if each value has a left neighbor
        # which is the value 1 lower

        # if not then it's the start of a sequence, and we can then check ascending right neighbor
        # if the right neigher exists, we can add 1 to the length of the sequence

        # and we can keep track of the max length

        # in our example, 2, 20, and 10 do not have left neighbors
        # (1, 19, and 9 are not in the set)
        # 20 and 10 have no right neighbors so the length of that seq is 1

        # 2 has a right number 3 then 4 then 5 so we can add 1 til we get length 4

        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest