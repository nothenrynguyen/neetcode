class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        return len(set(nums)) < len(nums)

        # this uses a set to get rid of duplicates.
        # if there were no duplicates, than the set
        # has the same length as the given array.
        # otherwise the set is shorter.

        # return True if the set is shorter (contains dupes)
