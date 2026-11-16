class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n) # saying this value n occurs exactly c times

        result = []

        for i in range(len(freq) -1, 0, -1): # descending order, going thru every value
            for n in freq[i]:
                result.append(n)

                if len(result) == k: # cuz we want the k most freq elements
                    return result