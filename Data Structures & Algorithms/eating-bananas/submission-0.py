class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        result = right

        # binary search ( range )
        
        while left <= right:
            k = (left + right) // 2     # "//" is floor division
            hours = 0

            for p in piles:
                hours += math.ceil(p / k)   # math.ceil gives us division rounded up

            if hours <= h:
                result = min(result, k)

                right = k - 1

            else:
                left = k + 1

        return result