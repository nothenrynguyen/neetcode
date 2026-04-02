class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)             # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26    # a ... z

            for c in s:                         # go thru every character in each string
                count[ord(c) - ord('a')] += 1   # and count how many of each character
                                                # for example, ascii of a is 97
                                                # but we want to map a -> 0 so we subtract 
                                                # ord("a") which is 97. all other letters ascend.

            result[tuple(count)].append(s)      # we use tuple cuz lists can't be keys in python
                                                # and tuples are nonmutable.

        return list(result.values())

            # this is the optimal O(m * n) solution where:
            # m is the number of strings we're given and
            # n is the average length of each string