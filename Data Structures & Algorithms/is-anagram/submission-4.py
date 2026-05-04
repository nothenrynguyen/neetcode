class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # this is a solution without using extra memory, so O(1)

        # a way is to sort them and just compare them if they are exact same string
        # but sorting depending on the algo can be up to n^2 or better nlogn which is still not amazing
        
        return sorted(s) == sorted(t)

        # not always faster but it does save on memory -> in case that's a followup question