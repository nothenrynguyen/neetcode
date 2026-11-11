class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a...z

            for c in s:
                count[ord(c) - ord("a")] += 1 # so its ascii of current character minus ascii of lowercase "a"

            result[tuple(count)].append(s)

        return list(result.values())

        # O(m*n) where m is the number of strings given and n is avg length of each string