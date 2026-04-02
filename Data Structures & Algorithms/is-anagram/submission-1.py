class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # solution 1 is making 2 hashmaps - 1 for S and 1 for T - and compare the two
        # this is O(S+T) for time and space for size of hashmap
        # there's another solution that solves this memory problem

        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        
        for i in range(len(s)): # we can iterate thru the length of the string since we know they are the same length at this point
            countS[s[i]] = 1 + countS.get(s[i], 0) # we use get to set a default value of 0 otherwise we get a key error
            countT[t[i]] = 1 + countT.get(t[i], 0)
            # and this is it for building the hashmap

        # now we need to iterate thru the hashmap
        for c in countS:
            if countS[c] != countT.get(c, 0): # we use get again in case in case the key c from countS doesn't exist in the T map
                return False

        return True

        # this is the same solution but using counter built-in in python
        # might not work for interviews tho but if i rememebr it it can be a cool trick
        # return Counter(s) == Counter(t) 
