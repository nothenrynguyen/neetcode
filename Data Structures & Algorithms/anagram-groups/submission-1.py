class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = defaultdict(list)
        result = []

        for s in strs:
            sortedString = tuple(sorted(s))
            anagram[sortedString].append(s)

        for value in anagram.values():
            result.append(value)

        return result